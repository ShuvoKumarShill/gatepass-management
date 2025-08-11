from django.db import models
import uuid


class GatePass(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    gate_pass_number = models.CharField(max_length=50, unique=True)
    visitor_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    purpose = models.TextField()
    date_of_entry = models.DateField()
    time_of_entry = models.TimeField()
    approved_by = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    notes = models.TextField(blank=True, null=True)
    visitor_photo = models.FileField(upload_to='visitor_photos/', blank=True, null=True)
    qr_code = models.FileField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return f'{self.gate_pass_number} - {self.visitor_name}'