from rest_framework import serializers
from gatepass.models import GatePass

class GatePassSerializer(serializers.ModelSerializer):
    class Meta:
        model = GatePass
        fields = [
            'gate_pass_number',
            'visitor_name',
            'organization',
            'contact_number',
            'purpose',
            'date_of_entry',
            'time_of_entry',
            'approved_by',
            'status',
            'notes',
            'visitor_photo',
            'qr_code',
        ]