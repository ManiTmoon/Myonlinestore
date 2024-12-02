from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),  # Add this line
    path('signup/', views.signup, name='signup'),
]
