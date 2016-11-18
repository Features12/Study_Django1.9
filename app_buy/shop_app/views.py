from django.shortcuts import render
from .models import Shop_List

def output(request):
    context = {
        "all_shop_list" : Shop_List.objects.all(),
               }
    return render(request, 'shop_app/index.html', context)


def garbage(request):
    return render(request, 'shop_app/garbage.html')


def items_details(request,id):
    context_details = {
        "details_name" : Shop_List.objects.get(id = id)
    }
    return render(request, 'shop_app/items_details.html', context_details)


def login(request):
    return render(request, 'shop_app/login.html')


def reg(request):
    return render(request, 'shop_app/reg.html')





