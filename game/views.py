from django.shortcuts import render
from game.models import Profile


def base(request):
    return render(request, 'base.html')


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profile.html', {'profile': profile})
