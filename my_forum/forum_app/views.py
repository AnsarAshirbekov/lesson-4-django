from django.shortcuts import render

def forum_view(request):
    return render(request, 'main.html')

def topics(request):
    return render(request, 'topics.html')

def profile(request):
    return render(request, 'profile.html')
