from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GatePassViewSet

router = DefaultRouter()
router.register(r'gatepass', GatePassViewSet, basename='gatepass')

urlpatterns = [
    path('gatepass/create/', GatePassViewSet.as_view({'post': 'create'}), name='gatepass-create'),
]

urlpatterns += router.urls