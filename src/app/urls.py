from django.contrib import admin
from django.urls import path, include
from .views import home
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),


    #Includes de usuarios
    path('usuario/', include('usuarios.urls')),



    #Includes de posts
    path('post/', include('posts.urls')),


    #Includes de comments
    path('comment/', include('comment.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
