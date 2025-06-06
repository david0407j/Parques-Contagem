from django.shortcuts import render


def base(request):
    return render(request, "base/home.html")


def parque_individual(request):
    return render(request, 'base/index.html')
