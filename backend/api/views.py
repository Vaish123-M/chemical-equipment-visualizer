from io import BytesIO

import pandas as pd
from django.http import FileResponse, Http404
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EquipmentDataset
from .serializers import EquipmentDatasetSerializer


REQUIRED_COLUMNS = {"flowrate", "pressure", "temperature", "type"}


def _cleanup_old_datasets():
    excess = EquipmentDataset.objects.order_by("-upload_time")[5:]
    for item in excess:
        if item.original_csv:
            item.original_csv.delete(save=False)
        item.delete()


def _build_report(dataset: EquipmentDataset) -> BytesIO:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    y = height - 60
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "Chemical Equipment Dataset Report")

    y -= 40
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, f"Dataset ID: {dataset.id}")
    y -= 20
    pdf.drawString(50, y, f"Upload time: {dataset.upload_time:%Y-%m-%d %H:%M:%S}")

    y -= 30
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Summary Statistics")

    y -= 20
    pdf.setFont("Helvetica", 11)
    pdf.drawString(60, y, f"Total count: {dataset.total_count}")
    y -= 18
    pdf.drawString(60, y, f"Average flowrate: {dataset.avg_flowrate:.2f}")
    y -= 18
    pdf.drawString(60, y, f"Average pressure: {dataset.avg_pressure:.2f}")
    y -= 18
    pdf.drawString(60, y, f"Average temperature: {dataset.avg_temperature:.2f}")

    y -= 30
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y, "Equipment Type Distribution")

    y -= 20
    pdf.setFont("Helvetica", 11)
    for equipment_type, count in dataset.type_distribution.items():
        pdf.drawString(60, y, f"{equipment_type}: {count}")
        y -= 18
        if y < 80:
            pdf.showPage()
            y = height - 60
            pdf.setFont("Helvetica", 11)

    pdf.showPage()
    pdf.save()
    buffer.seek(0)
    return buffer


class UploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        csv_file = request.FILES.get("file")
        if not csv_file:
            return Response({"detail": "CSV file is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            dataframe = pd.read_csv(csv_file)
            csv_file.seek(0)
        except Exception as exc:
            return Response({"detail": f"Unable to parse CSV: {exc}"}, status=status.HTTP_400_BAD_REQUEST)

        missing = REQUIRED_COLUMNS.difference(dataframe.columns)
        if missing:
            return Response(
                {"detail": f"Missing required columns: {', '.join(sorted(missing))}"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        total_count = int(len(dataframe))
        avg_flowrate = float(dataframe["flowrate"].mean()) if total_count else 0.0
        avg_pressure = float(dataframe["pressure"].mean()) if total_count else 0.0
        avg_temperature = float(dataframe["temperature"].mean()) if total_count else 0.0
        type_distribution = dataframe["type"].value_counts().to_dict()

        dataset = EquipmentDataset.objects.create(
            original_csv=csv_file,
            total_count=total_count,
            avg_flowrate=avg_flowrate,
            avg_pressure=avg_pressure,
            avg_temperature=avg_temperature,
            type_distribution=type_distribution,
        )
        _cleanup_old_datasets()

        serializer = EquipmentDatasetSerializer(dataset)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SummaryView(APIView):
    def get(self, request, dataset_id):
        try:
            dataset = EquipmentDataset.objects.get(id=dataset_id)
        except EquipmentDataset.DoesNotExist as exc:
            raise Http404("Dataset not found") from exc

        serializer = EquipmentDatasetSerializer(dataset)
        return Response(serializer.data)


class HistoryView(APIView):
    def get(self, request):
        datasets = EquipmentDataset.objects.order_by("-upload_time")[:5]
        serializer = EquipmentDatasetSerializer(datasets, many=True)
        return Response(serializer.data)


class ReportView(APIView):
    def get(self, request, dataset_id):
        try:
            dataset = EquipmentDataset.objects.get(id=dataset_id)
        except EquipmentDataset.DoesNotExist as exc:
            raise Http404("Dataset not found") from exc

        buffer = _build_report(dataset)
        filename = f"dataset_{dataset.id}_report.pdf"
        return FileResponse(buffer, as_attachment=True, filename=filename)
