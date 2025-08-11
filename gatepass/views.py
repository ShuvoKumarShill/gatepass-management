from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import GatePass
from .forms import GatePassForm
from django.http import JsonResponse


class GatePassListView(View):
    def get(self, request):
        gatepasses = GatePass.objects.all()
        return render(request, 'gatepass/gatepass_list.html', {'gatepasses': gatepasses})


class GatePassDetailView(View):
    def get(self, request, pk):
        gatepass = get_object_or_404(GatePass, pk=pk)
        return render(request, 'gatepass/gatepass_detail.html', {'gatepass': gatepass})


class GatePassCreateView(View):
    def get(self, request):
        form = GatePassForm()
        return render(request, 'gatepass/gatepass_create.html', {'form': form})

    def post(self, request):
        form = GatePassForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gatepass_list')
        return render(request, 'gatepass/gatepass_create.html', {'form': form})


class GatePassVerifyView(View):
    def get(self, request, pk):
        gatepass = get_object_or_404(GatePass, pk=pk)
        return render(request, 'gatepass/gatepass_verify.html', {'gate_pass': gatepass})


class GatePassAPI(View):
    def get(self, request):
        gatepasses = GatePass.objects.all().values()
        return JsonResponse(list(gatepasses), safe=False)