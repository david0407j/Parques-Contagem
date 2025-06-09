from django.shortcuts import render


def base(request):
    return render(request, "base/home.html")


def parque_layout_1(request):
    return render(request, 'base/layout_1.html')


def parque_layout_2(request):
    return render(request, 'base/index.html')
