# from django.shortcuts import render
from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    print('home')
    return HttpResponse('home do app 1')