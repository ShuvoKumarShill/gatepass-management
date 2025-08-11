from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from gatepass.models import GatePass
from django.contrib.auth import get_user_model

User = get_user_model()

class GatePassAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.gate_pass_data = {
            'gate_pass_number': 'GP12345',
            'visitor_name': 'John Doe',
            'organization': 'Example Corp',
            'contact_number': '1234567890',
            'purpose': 'Meeting',
            'date_of_entry': '2023-10-01',
            'time_of_entry': '10:00',
            'approved_by': self.user.id,
            'status': 'Approved',
            'notes': 'N/A',
            'visitor_photo': None,  # Assuming photo upload is handled separately
            'qr_code': None,  # Assuming QR code generation is handled separately
        }

    def test_create_gate_pass(self):
        response = self.client.post(reverse('gatepass-create'), self.gate_pass_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GatePass.objects.count(), 1)
        self.assertEqual(GatePass.objects.get().visitor_name, 'John Doe')

    def test_list_gate_passes(self):
        GatePass.objects.create(**self.gate_pass_data)
        response = self.client.get(reverse('gatepass-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_gate_pass(self):
        gate_pass = GatePass.objects.create(**self.gate_pass_data)
        response = self.client.get(reverse('gatepass-detail', args=[gate_pass.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['visitor_name'], 'John Doe')

    def test_update_gate_pass(self):
        gate_pass = GatePass.objects.create(**self.gate_pass_data)
        updated_data = {'visitor_name': 'Jane Doe'}
        response = self.client.patch(reverse('gatepass-detail', args=[gate_pass.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        gate_pass.refresh_from_db()
        self.assertEqual(gate_pass.visitor_name, 'Jane Doe')

    def test_delete_gate_pass(self):
        gate_pass = GatePass.objects.create(**self.gate_pass_data)
        response = self.client.delete(reverse('gatepass-detail', args=[gate_pass.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(GatePass.objects.count(), 0)