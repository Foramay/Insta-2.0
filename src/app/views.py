from django.shortcuts import render
from posts.models import Posts

def home(request):
    template_name = 'home.html'
    #Acá creamos una variable que contiene todos los registros del modelo 'Posts' para pasarlo en el context
    posts = Posts.objects.all()
    ctx = {
        'posts': posts
    }
    return render(request, template_name, ctx)

