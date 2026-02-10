from django.urls import path

from .views import HistoryView, ReportView, SummaryView, UploadView

urlpatterns = [
    path("upload/", UploadView.as_view(), name="upload"),
    path("summary/<int:dataset_id>/", SummaryView.as_view(), name="summary"),
    path("history/", HistoryView.as_view(), name="history"),
    path("report/<int:dataset_id>/", ReportView.as_view(), name="report"),
]
