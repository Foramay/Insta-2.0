from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Posts
from django.urls import reverse
from .forms import PostForm

class CreatePost(LoginRequiredMixin, CreateView):
    model = Posts
    form_class = PostForm
    template_name = 'posts/crear_post.html'

    
    def form_valid(self, form):
        #Con esta función lo que estamos haciendo es que obtenemos automáticamente el id del usuario logueado para que pueda hacer la publicación sin usar el formulario de creación, este nos evita por ejemplo como elegir el usuario con el que querramos crear la publicación.
        form.instance.usuario = self.request.user  # Obtenemos el nombre del usuario
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('home')