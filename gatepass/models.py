from django.db import models
import qrcode
from django.core.files.base import ContentFile
import uuid

class GatePass(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    gate_pass_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    visitor_name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    purpose = models.TextField()
    date_of_entry = models.DateField()
    time_of_entry = models.TimeField()
    approved_by = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, null=True)
    visitor_photo = models.ImageField(upload_to='visitor_photos/', blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.qr_code:
            qr_data = str(self.gate_pass_number)
            qr_image = qrcode.make(qr_data)
            qr_image_file = ContentFile(qr_image.tobytes())
            self.qr_code.save(f'qr_{self.gate_pass_number}.png', qr_image_file, save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Gate Pass {self.gate_pass_number} - {self.visitor_name}'