from django.shortcuts import render
from .models import Shop_List
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
        "all_shop_list": Shop_List.objects.all(),
    }
    return render(request, 'shop_app/garbage.html', context)


# Детальная страница отображения продуктов из index.html
def items_details(request,id):
    context_details = {
        "details_name" : Shop_List.objects.get(id = id),
        "details_output" : Shop_List.objects.filter(id = id).first(),
        "username": auth.get_user(request).username,
    }
    return render(request, 'shop_app/items_details.html', context_details)

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





