from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('follow/<str:username>', views.follow, name='follow'),
    path('unfollow/<str:username>', views.unfollow, name='unfollow')
]
