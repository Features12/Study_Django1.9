from django.shortcuts import render, render_to_response, HttpResponse
from .models import Shop_List, Shop_Cart, News
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.shortcuts import  redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import auth
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# Основаная страница index.html
def news_page(request):
    news = News.objects.all()
    paginator = Paginator(news, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)
    context = {
        "username": auth.get_user(request).username,
        "all_news": news,#[0:9],

    }
    return render(request,'shop_app/index.html', context)


def news_details(request, id):
    if request.POST:
        com_text = request.POST['text']
        News.objects.create(comments=com_text)
    context = {
        "username": auth.get_user(request).username,
        "details_name": News.objects.get(id=id),
        "details_output": News.objects.filter(id=id).first(),
    }

    return render(request, 'shop_app/news_details.html', context)


# Отображение всех товаров на сайте
def shop_output_list(request):
    list = Shop_List.objects.all()
    paginator = Paginator(list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list = paginator.page(paginator.num_pages)
    context = {
        "all_shop_list" : list,
        "username" : auth.get_user(request).username,
               }
    return render(request, 'shop_app/shop.html', context)


# Корзина
def garbage(request):
    list = Shop_Cart.objects.all()
    paginator = Paginator(list, 10)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        list = paginator.page(paginator.num_pages)
    context = {
        "all_cart_list": list,
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
    Shop_Cart.objects.create(
        user=request.user,
        product_id=id,
        quantity_product=1,
        state_product="add")
    """x = Shop_List.objects.filter() # список всех объектов
    for i in x:
        a = i.id # получаем id каждого объекта(1,2,3,4,5,6,7)
        b = Shop_Cart.objects.filter(user = request.user, product_id = a).first()
        if b:
            b.quantity_product += 1
            b.save()
        else:
            Shop_Cart.objects.create(
            user=request.user,
            product_id=id,
            quantity_product=1,
            state_product="add")"""

    context = {
        "shop_list": Shop_Cart.objects.filter(user=request.user),
        "username": auth.get_user(request).username,
        "details_name": Shop_List.objects.get(id=id),
        "details_output": Shop_List.objects.filter(id=id).first(),
    }

    return render(request, 'shop_app/garbage.html', context)


# Детальная страница отображения продуктов из shop.html
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
            return redirect("/") #возвращает на index.html
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





