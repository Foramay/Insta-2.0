
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después del registro
            return redirect('home')  # Redirige a la página de inicio o a cualquier otra página deseada
    else:
        form = UserRegisterForm()
    return render(request, 'usuarios/register.html', {'form': form})

@login_required
def profile(request):
    template_name = 'usuarios/profile.html'
    return render(request, template_name, {})