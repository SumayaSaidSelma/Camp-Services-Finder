from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from django.contrib.auth import login, authenticate
from .forms import ServiceForm, CustomUserCreationForm 
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LogoutView


def service_list(request):
    query = request.GET.get('q')
    if query:
        services = Service.objects.filter(
            Q(name__icontains=query) | 
            Q(category__icontains=query) | 
            Q(location__icontains=query) |
            Q(hours__icontains=query)
        )
    else:
        services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services': services})


@user_passes_test(lambda u: u.is_staff)
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list') 
    else:
        form = ServiceForm()

    return render(request, 'services/add_service.html', {'form': form})

def home(request):
    return render(request, 'services/home.html')

def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'services/service_detail.html', {'service': service})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = request.POST.get('is_admin') == 'on'
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            login(request, user)
            return redirect('service_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'services/register.html', {'form': form})


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('service_list')  
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'services/login.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def create_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form})


class ServiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_update.html'
    success_url = reverse_lazy('service_list')

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('login')



class ServiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Service
    template_name = 'services/service_confirm_delete.html'
    success_url = reverse_lazy('service_list')

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('login')

class CustomLogoutView(LogoutView):
    next_page = 'login'