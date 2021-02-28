from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    # Pretend this data came from the model and database
    missions = [
        "ISS Resupply Mission - 04 March 2021",
        "Perseverence Driving Test - Mars - 10 March 2021",
        "Hubble Space Telescope Repairs - LEO - 21 March 2021",
        "Play with puppies in space",
        "Get drunk in space",
        "Play guitar in space"
    ]

    context = {
        'all_missions': missions,
        'director': 'Paul Tomkins'
    }

    html_page = render(request, 'home.html', context)

    return html_page


def elon(request):
    return render(request, 'elon.html')