# app/urls.py


from django.urls import path
from . import views

urlpatterns = [
    path('print/', views.print_prn, name='print'),
]

