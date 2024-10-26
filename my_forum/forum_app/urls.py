from django.urls import path
from .views import forum_view, topics, profile

urlpatterns = [
    path('', forum_view, name='forum'),
    path('topics', topics, name='topics'),
    path('profile', profile, name='profile')
]