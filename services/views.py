

from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def service_list(request):
    services = Service.objects.all()
    # print(services)  # Check if services contains data
    return render(request, 'services/service_list.html', {'services': services})

def home(request): #home page
    return render(request, 'services/home.html')


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})

#registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('/') # Redirect after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})