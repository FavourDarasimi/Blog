from django.urls import path
from .views import SignupView,CreateProfileView,EditProfile
from . import views

urlpatterns = [
    path('signup/',SignupView.as_view(),name='signup'),
    path('create_profile/',CreateProfileView.as_view(),name='create_profile'),
    path('profile/',views.profile_view,name='profile'),
    path('profile/edit/<int:pk>',EditProfile.as_view(),name='edit_profile')
]