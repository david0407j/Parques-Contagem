from django.shortcuts import render


def base(request):
    return render(request, "base/home.html")


def parque_1(request):
    return render(request, "base/parque_1.html")


def parque_2(request):
    return render(request, "base/parque_2.html")


def parque_3(request):
    return render(request, "base/parque_3.html")
