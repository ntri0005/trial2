from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import trialTableSerializer, HospitalTableSerializer, BeachTableSerializer
from .models import trialTable, HospitalTable, BeachTable


# Create your views here.

class HospitalTableViewSet(viewsets.ModelViewSet):
	queryset = HospitalTable.objects.all()
	serializer_class = HospitalTableSerializer
	
class BeachTableViewSet(viewsets.ModelViewSet):
	queryset = BeachTable.objects.all()
	serializer_class = BeachTableSerializer

class trialTableViewSet(viewsets.ModelViewSet):
	queryset = trialTable.objects.all()
	serializer_class = trialTableSerializer

def homepage(request):
	return HttpResponse("<strong>IE Project</strong>")