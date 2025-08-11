from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from gatepass.models import GatePass
from .serializers import GatePassSerializer


class GatePassViewSet(viewsets.ModelViewSet):
    queryset = GatePass.objects.all()
    serializer_class = GatePassSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=True, methods=['get'])
    def verify(self, request, pk=None):
        gate_pass = self.get_object()
        return Response({
            'gate_pass_number': gate_pass.gate_pass_number,
            'visitor_name': gate_pass.visitor_name,
            'status': gate_pass.status,
            'qr_code': gate_pass.qr_code.url if gate_pass.qr_code else None,
        })