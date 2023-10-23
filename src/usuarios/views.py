
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from posts.models import Posts
from .models import Usuario, Relationship
from django.http import HttpResponseRedirect
from django.urls import reverse

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
def profile(request, username=None):
    #Acá le decimos con que html vamos a trabajar
    template_name = 'usuarios/profile.html'
    #Obtenemos el username del usuario logueado
    user_logueado = request.user
    if username and username != user_logueado.username:
    #Verificamos si el username es el mismo que el username logueado
        #Instanciamos el modelo Usuario para obtener el username
        user = Usuario.objects.get(username=username)
        #Obtenemos todos los posts del usuario mediante el id 
        posts = Posts.objects.filter(usuario_id=user.id)
    else:
    #Y si no es el mismo, mostramos esto
        user = user_logueado
        posts = Posts.objects.filter(usuario_id=user_logueado.id)


        
    return render(request, template_name, {'user': user, 'posts': posts})


def follow(request, username):
    current_user = request.user
    to_user = Usuario.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    return HttpResponseRedirect(reverse('user:profile', kwargs={'username': username}))

def unfollow(request, username):
    current_user = request.user
    to_user = Usuario.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    return HttpResponseRedirect(reverse('user:profile', kwargs={'username': username}))