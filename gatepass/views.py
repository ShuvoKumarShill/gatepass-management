from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import GatePass
from .forms import GatePassForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse

class GatePassListView(LoginRequiredMixin, View):
    def get(self, request):
        gatepasses = GatePass.objects.all()
        return render(request, 'gatepass/gatepass_list.html', {'gatepasses': gatepasses})

class GatePassDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        gatepass = get_object_or_404(GatePass, pk=pk)
        return render(request, 'gatepass/gatepass_detail.html', {'gatepass': gatepass})

class GatePassCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = GatePassForm()
        return render(request, 'gatepass/gatepass_create.html', {'form': form})

    def post(self, request):
        form = GatePassForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gatepass_list')
        return render(request, 'gatepass/gatepass_create.html', {'form': form})

class GatePassVerifyView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        return render(request, 'gatepass/gatepass_verify.html')

class GatePassAPI(View):
    def get(self, request):
        gatepasses = GatePass.objects.all().values()
        return JsonResponse(list(gatepasses), safe=False)