from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Profile



class SignupView(CreateView):
    form_class=UserCreationForm
    template_name="registration/signup.html"
    success_url=reverse_lazy("login")

class CreateProfileView(CreateView):
    model=Profile
    template_name="profile/create_profile.html"
    fields=("first_name","last_name","email","age","gender","bio","picture")
    success_url=reverse_lazy("profile")
    
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
def profile_view(request):
    context={}
    return render(request,"profile/profile_view.html",context)   

class EditProfile(UpdateView):
    model=Profile
    template_name="profile/edit_profile.html"
    fields=("first_name","last_name","email","age","gender","bio","picture")
    success_url=reverse_lazy("profile")

   
        


# Create your views here.
