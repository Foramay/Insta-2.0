from django.urls import path
from . import views

urlpatterns = [
    path('crear_post/', views.CreatePost.as_view(), name='crear_post')
]
