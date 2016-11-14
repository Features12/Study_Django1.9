from django.shortcuts import render


def output(request):
    return render(request, 'shop_app/index.html')


def garbage(request):
    return render(request, 'shop_app/garbage.html')


def items_details(request):
    return render(request, 'shop_app/items_details.html')


def login(request):
    return render(request, 'shop_app/login.html')


def reg(request):
    return render(request, 'shop_app/reg.html')


