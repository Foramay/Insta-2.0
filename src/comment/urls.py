from django.urls import path
from .views import comment

app_name = 'comments'


urlpatterns = [
    path('comment/<int:pk>', comment, name='comment')
]
