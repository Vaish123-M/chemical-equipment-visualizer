from django.db import models


class EquipmentDataset(models.Model):
    upload_time = models.DateTimeField(auto_now_add=True)
    original_csv = models.FileField(upload_to="uploads/")
    total_count = models.IntegerField()
    avg_flowrate = models.FloatField()
    avg_pressure = models.FloatField()
    avg_temperature = models.FloatField()
    type_distribution = models.JSONField()

    class Meta:
        ordering = ["-upload_time"]

    def __str__(self):
        return f"Dataset {self.id} ({self.upload_time:%Y-%m-%d %H:%M:%S})"
