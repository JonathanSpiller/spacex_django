from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Mission
from django.http import Http404

def home(request):

    missions = Mission.objects.all()

    context = {
        'all_missions': missions,
        'director': 'Paul Tomkins'
    }

    html_page = render(request, 'home.html', context)

    return html_page


def elon(request):
    return render(request, 'elon.html')


def mission(request, id):
    try:
        mission = get_object_or_404(Mission, pk=id)
        return render(request, 'mission_details.html', {'mission': mission})
    except Http404:
        return render(request, '404.html')
        

def tesla(request):
    return redirect("http://tesla.com")

