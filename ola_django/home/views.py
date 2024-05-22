from django.shortcuts import render


def home(request):
    print('home')

    return render(
        request,
        'home/index.html'
    )




def exemplo(request):
    print('exemplo')
    return render(
        request,
        'home/exemplo.html'
    )