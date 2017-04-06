from django.contrib import admin
from django.db import models
from django.forms import widgets
from .models import Student, Group
from django.forms.widgets import SelectDateWidget


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fieldsets =  [ # должны быть отключены модифицирующие/группирующие поля виджеты
        (None, {'fields':['name', 'surname']}), #title = None, fields: name, surname
        ('More information', {'fields': ['email'], #title = More information, fields: email,
                              'classes': ['collapse']}), # classes: collapse (скрыть/раскрыть меню)
    ]
    date_hierarchy = 'date_of_birth' # отобразить в админке сверху списка даты(года) указанного поля
    list_display = ['name', 'surname', 'group'] # отобразит в листинге данные поля
    list_display_links = ['name', 'surname', 'group'] # подстветит отображение, как ссылки данных полей
    list_max_show_all = 200 # сколько всего отобразить в списке объектов
    list_per_page = 20 # пагинация (отобразить на странице такое кол-во объектов)
    ordering = ['name', 'group'] # приоритет сортировки в алфавитном порядке: 1, 2, 3
    list_filter = ['name', 'email', 'package', 'group'] # добавляет виджет с фильтрами по данным полям
    search_fields = ['name', 'group__name'] # добавляет строку-виджет поиска



class StudentInline(admin.StackedInline):
    model = Student # имя модели, которая будет ссылаться в другую модель в админке по ForeignKey
    fk_name = 'group' # ForeignKey поле
    fields = ['name', 'surname', 'package'] # какие поля показывать

@admin.register(Group) # регистрация модели в админке
class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline] # перечислить классы, которые ссылаются на данный класс в админке