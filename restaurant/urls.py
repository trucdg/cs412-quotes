# restaurant/urls.py


from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.main, name='main'),
    path(r'order/', views.order, name='order'),
    path(r'submit/', views.submit, name="submit")
    #path(r'confirmation/', views.confirmation, name='confirmation'),
]