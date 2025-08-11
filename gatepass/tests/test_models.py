from django.test import TestCase
from .models import GatePass

class GatePassModelTest(TestCase):

    def setUp(self):
        self.gate_pass = GatePass.objects.create(
            gate_pass_number="GP123456",
            visitor_name="John Doe",
            organization="Example Corp",
            contact_number="1234567890",
            purpose="Business Meeting",
            date_of_entry="2023-10-01",
            time_of_entry="09:00",
            approved_by="Admin",
            status="Approved",
            notes="N/A",
            visitor_photo="path/to/photo.jpg",
            qr_code="path/to/qr_code.png"
        )

    def test_gate_pass_creation(self):
        self.assertEqual(self.gate_pass.gate_pass_number, "GP123456")
        self.assertEqual(self.gate_pass.visitor_name, "John Doe")
        self.assertEqual(self.gate_pass.organization, "Example Corp")
        self.assertEqual(self.gate_pass.contact_number, "1234567890")
        self.assertEqual(self.gate_pass.purpose, "Business Meeting")
        self.assertEqual(str(self.gate_pass.date_of_entry), "2023-10-01")
        self.assertEqual(self.gate_pass.time_of_entry, "09:00")
        self.assertEqual(self.gate_pass.approved_by, "Admin")
        self.assertEqual(self.gate_pass.status, "Approved")
        self.assertEqual(self.gate_pass.notes, "N/A")
        self.assertEqual(self.gate_pass.visitor_photo, "path/to/photo.jpg")
        self.assertEqual(self.gate_pass.qr_code, "path/to/qr_code.png")

    def test_gate_pass_str(self):
        self.assertEqual(str(self.gate_pass), "GP123456 - John Doe")