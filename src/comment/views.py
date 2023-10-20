from django.shortcuts import render, redirect
from posts.models import Posts
from .models import Comment
from django.contrib.auth.decorators import login_required

@login_required
def comment(request, pk):
    if request.method == 'POST':
        #Acá lo que estamos haciendo es recuperar el comentario que deja el usuario logueado a través del formulario
        comment = request.POST.get('comment')
        #Acá obtenemos el objeto del modelo Post que contiene el id
        post = Posts.objects.get(pk=pk)
        #Acá guardamos en una variable solamente el id del post
        post_id = post.id
        #Acá guardamos el id del usuario logueado
        user_id = request.user.id
        #Instanciamos el modelo de Comment
        instance_comment_model = Comment(comment=comment, post_id=post_id, user_id=user_id)
        #Guardamos el comentario en la base de datos
        instance_comment_model.save()
    return redirect('home')

