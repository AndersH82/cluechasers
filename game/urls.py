from django.urls import path
from. import views
from.views import login_view

urlpatterns = [
    path('', views.base, name='base'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
]