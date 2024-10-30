from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Event
# Create your views here.


def event_list(request):
    events = Event.objects.all()
    data = {'events': events}
    return render(request, 'agenda.html', data)


