from django.urls import path
from . import views

urlpatterns = [
    path('', views.GatePassListView.as_view(), name='gatepass_list'),
    path('create/', views.GatePassCreateView.as_view(), name='gatepass_create'),
    path('<int:pk>/', views.GatePassDetailView.as_view(), name='gatepass_detail'),
    path('verify/<int:pk>/', views.GatePassVerifyView.as_view(), name='gatepass_verify'),
]