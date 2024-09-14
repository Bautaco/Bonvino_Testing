from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def Home (request):
    return render (request, 'Maridaje_App/Home.html')

@login_required
def Vino (request):
    return render (request, 'Maridaje_App/Vino.html')

@login_required
def Comida (request):
    return render (request, 'Maridaje_App/Comida.html')

@login_required
def Maridaje (request):
    return render (request, 'Maridaje_App/Maridaje.html')