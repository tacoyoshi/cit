from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from stations.models import Station

# Create your views here.

class StationList(ListView):
    model = Station
    context_object_name = 'stations'

class StationView(DetailView):
    model = Station
    context_object_name = 'station'

class StationCreate(CreateView):
    model = Station
    fields = ['station_code', 'station_name']
    context_object_name = 'station'

class StationUpdate(UpdateView):
    model = Station
    fields = ['station_code', 'station_name']
    context_object_name = 'station'

class StationDelete(DeleteView):
    model = Station
    context_object_name = 'station'
    success_url = reverse_lazy('station-list')
