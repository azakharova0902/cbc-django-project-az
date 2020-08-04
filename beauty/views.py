from django.shortcuts import render
from django.http import HttpResponse

from .models import Service
from .models import Technician

from django.http import Http404

def home(request):
    return render(request, 'home.html')

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services,})

def service_details(request, service_id):
    try:
        service = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        raise Http404('ooops..looks like the service was not round')
    return render (request, 'service_details.html', {'service': service,})


def team(request):
    team = Technician.objects.all()
    return render(request, 'team.html', {'team': team,})
