from django.test import TestCase
from django.urls import reverse
from gatepass.models import GatePass


class GatePassViewTests(TestCase):

    def setUp(self):
        self.gate_pass = GatePass.objects.create(
            gate_pass_number="GP123",
            visitor_name="John Doe",
            organization="Example Corp",
            contact_number="1234567890",
            purpose="Meeting",
            date_of_entry="2023-10-01",
            time_of_entry="10:00",
            approved_by="Admin",
            status="Approved",
            notes="N/A",
            visitor_photo=None,  # Assuming photo upload is handled separately
            qr_code=None  # Assuming QR code generation is handled separately
        )

    def test_gatepass_list_view(self):
        response = self.client.get(reverse('gatepass_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.gate_pass.visitor_name)
        self.assertTemplateUsed(response, 'gatepass/gatepass_list.html')

    def test_gatepass_detail_view(self):
        response = self.client.get(reverse('gatepass_detail', args=[self.gate_pass.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.gate_pass.visitor_name)
        self.assertTemplateUsed(response, 'gatepass/gatepass_detail.html')

    def test_gatepass_create_view(self):
        response = self.client.post(reverse('gatepass_create'), {
            'gate_pass_number': 'GP124',
            'visitor_name': 'Jane Smith',
            'organization': 'Another Corp',
            'contact_number': '0987654321',
            'purpose': 'Interview',
            'date_of_entry': '2023-10-02',
            'time_of_entry': '11:00',
            'approved_by': 'Admin',
            'status': 'Pending',
            'notes': 'N/A',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        self.assertTrue(GatePass.objects.filter(visitor_name='Jane Smith').exists())

    def test_gatepass_verify_view(self):
        response = self.client.get(reverse('gatepass_verify', args=[self.gate_pass.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.gate_pass.gate_pass_number)
        self.assertTemplateUsed(response, 'gatepass/gatepass_verify.html')