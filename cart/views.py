from django.shortcuts import render


def detail(request):
    return render(request, 'cart/detail.html')
