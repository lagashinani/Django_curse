import csv
import urllib

from django.shortcuts import render, redirect
from django.urls import reverse

from .settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = 1
    bus_stations_data = []
    prev_page_url = None
    next_page_url = None

    if request.GET.get('page') is not None \
            and request.GET.get('page').isdigit() \
            and int(request.GET.get('page')) > 1:
        current_page = int(request.GET.get('page'))
        prev_page_url = reverse('bus_stations') + '?' + urllib.parse.urlencode({'page': current_page - 1})

    with open(BUS_STATION_CSV, newline='', encoding='cp1251') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            bus_stations_data.append(row)

    if len(bus_stations_data) > current_page * 10:
        next_page_url = reverse('bus_stations') + '?' + urllib.parse.urlencode({'page': current_page + 1})

    return render(request, 'index.html', context={
        'bus_stations': bus_stations_data[(current_page - 1) * 10:current_page * 10],
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

