from django.urls import path
from. import views

urlpatterns = [
    path('moh/', views.front, name='front'),
]