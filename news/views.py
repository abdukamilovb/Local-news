from django.shortcuts import render
from django.http import HttpResponse




def index(request):
    return render(request, 'signin.html')


def signup(request):
    return render(request, 'signup.html')  # signup.html sahifasini qaytarish
