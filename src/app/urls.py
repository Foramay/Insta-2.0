from django.contrib import admin
from django.urls import path
from .views import home
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login')
]
