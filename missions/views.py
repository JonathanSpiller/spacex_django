from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Mission, Astro, Rocket
from django.http import Http404
from cprint import cprint
from .forms import AddAstroForm, AddMissionForm, AddRocketForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

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
    # mission = get_object_or_404(Mission, pk=id)
    # return render(request, 'mission_details.html', {'mission': mission})
    try:
        mission = get_object_or_404(Mission, pk=id)
        return render(request, 'mission_details.html', {'mission': mission})
    except Http404:
        return render(request, '404.html')
        

def tesla(request):
    return redirect("http://tesla.com")


def astronauts(request):
    return render(request, 'astronauts.html', {'astronauts': Astro.objects.all()})


# Handled with Regular Forms
def add_astro(request):

    if request.method == "GET":
        myform = AddAstroForm()
        return render(request, 'add_astro.html', {'myform':myform})

    if request.method == "POST":

        myform = AddAstroForm(request.POST)

        if myform.is_valid():
            first_name=myform.cleaned_data['first_name']
            last_name=myform.cleaned_data['last_name']
            age=myform.cleaned_data['age']
            rank=myform.cleaned_data['rank']
            
            a1 = Astro(first_name=first_name, last_name=last_name, age=age, rank=rank)
            a1.save()

            return redirect('astronauts')

        else:
            return render(request, 'add_astro.html', {'myform':myform})


# Handled with Model Forms
def add_mission(request):

    if request.method == "GET":
        return render(request, 'add_mission.html', {'form': AddMissionForm()})

    if request.method == "POST":
        form = AddMissionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'add_mission.html', {'form': form})


class AllRockets(ListView):
    model = Rocket
    template_name = "rockets.html"

    #OPTIONAL CHANGES
    ordering = ['name']
    queryset = Rocket.objects.filter(fuel_capacity__gt=-1)


class RocketDeets(DetailView):
    model = Rocket
    template_name = "rocket_deets.html"
    
    # OPTIONALLY OVERRIDE get_context_data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = "SpaceX is the best!"
        return context


class AddRocket(CreateView):
    form_class = AddRocketForm
    template_name = 'add_rocket.html'
    success_url = reverse_lazy('see-rockets')
