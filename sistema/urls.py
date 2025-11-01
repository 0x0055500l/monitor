from django.urls import path
from . import views

urlpatterns = [
    path('', views.sistema_view, name='sistema'),
]
