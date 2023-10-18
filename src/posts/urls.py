from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('crear_post/', views.CreatePost.as_view(), name='crear_post'),
    path('update_post/<int:pk>', views.UpdatePost.as_view(), name='update_post')
]
