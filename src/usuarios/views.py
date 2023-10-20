
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from posts.models import Posts

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
    #Acá le decimos con que html vamos a trabajar
    template_name = 'usuarios/profile.html'
    #Acá recuperamos el id del usuario logueado
    user_id = request.user.id
    #Filtramos todos los posts del usuario logueado
    user_posts = Posts.objects.filter(usuario_id=user_id)

    #Y lo pasamos a través de un contexto
    context = {
        'user_posts': user_posts,
    }
    return render(request, template_name, context)