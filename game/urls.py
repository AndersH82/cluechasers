from django.urls import path
from. import views
from.views import login_view

urlpatterns = [
    path('', views.base, name='base'),
    path('profile/', views.profile, name='profile'),
    path('login/', login_view, name='login'),
]