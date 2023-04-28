from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(requset):
    return render (requset, 'signup.html')