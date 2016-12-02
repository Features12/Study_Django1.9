from django.shortcuts import render, render_to_response
from .models import Shop_List, Shop_Cart
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from django.core.context_processors import csrf
from django.shortcuts import  redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from django.contrib.auth import logout




# Основаная страница index.hrml
# Отображение всех товаров на сайте
def output(request):
    context = {
        "all_shop_list" : Shop_List.objects.all(),
        "username" : auth.get_user(request).username,
               }
    return render(request, 'shop_app/index.html', context)


# Корзина
def garbage(request):
    context = {
        "username": auth.get_user(request).username,
        "output_cart" : Shop_Cart.objects.filter(user = request.user),
        "cart_list" : Shop_Cart.objects.filter(user = request.user, state_product = "add"),
        "sum" : 0,
    }
    for element in context["cart_list"]:
        context["sum"] += element.product.price

    return render(request, 'shop_app/garbage.html', context)


# Функция покупки всех товаров (статус из add в buy)
def buy_items(request):
    context = {
        "buy": Shop_Cart.objects.filter(user=request.user, state_product="add").update(state_product = "buy"),
    }
    return render(request, "shop_app/garbage.html", context)


def shop_cart(request,id):
    a = Shop_List.objects.all().values("name", flat = True)
    count = Shop_Cart.objects.filter(user = request.user, name = a)
    if a in count:
        count.quantity_product += 1
        count.save()
    else:
        Shop_Cart.objects.create(
        user=request.user,
        product_id=id,
        quantity_product=1,
        state_product="add")

    context = {
        "shop_list": Shop_Cart.objects.filter(user=request.user),
        "username": auth.get_user(request).username,
        "details_name": Shop_List.objects.get(id=id),
        "details_output": Shop_List.objects.filter(id=id).first(),
    }

    return render(request, 'shop_app/garbage.html', context)


# Детальная страница отображения продуктов из index.html
def items_details(request,id):
    context = {
        "details_name" : Shop_List.objects.get(id = id),
        "details_output" : Shop_List.objects.filter(id = id).first(),
        "username": auth.get_user(request).username,
    }
    return render(request, 'shop_app/items_details.html', context)


# Авторизация пользователя через стандартную форму Django
def logins(request):
    args = {}
    args.update(csrf(request))
    args["form"] = AuthenticationForm()
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        newuser_form = AuthenticationForm(request.POST)
        user = auth.authenticate(username= username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/") #возвращает на index.html (main page)
        else:
            args["form"] = newuser_form
    return render(request, 'shop_app/login.html',args)


# Выход пользователя с авторизации
def logout_view(request):
    logout(request)
    return redirect("/")


# Регистрация пользователя через стандартную форму Django
def reg(request):
    args = {}
    args.update(csrf(request))
    args["form"] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username = newuser_form.cleaned_data["username"],
                                             password = newuser_form.cleaned_data["password2"])
            auth.login(request,newuser)
            return redirect("/")
        else:
            args["form"] = newuser_form
    return render(request, 'shop_app/reg.html', args)





