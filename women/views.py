from django.shortcuts import render
from django.http import HttpResponse
from women.models import Women

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


def index(request):
    posts = Women.objects.all()
    data = {'menu': menu, 'title': 'Главная страница', 'posts':posts}
    return render(request, "index.html", data)


def about(request):
    # posts = Women.objects.all()
    data = {'menu': menu, 'title': 'О сайте'}
    return render(request, 'index.html', data)


# from django.shortcuts import render
# from django.http import HttpResponse

# CRUD - Create, Retrive, Update, Delete
# Create - post запрос
# Retrive - get запрос
# Update - put запрос
# Delete -

# def index(request):
#     data = {"header": "Hello Django", "message": "Welcome to python"}
#     return render(request, "index.html", context=data)
#
# def index(request):
#     header = "Данные пользователя"  # обычная переменная
#     langs = ["Python", "Java", "C#"]  # список
#     user = {"name": "Tom", "age": 23}  # словарь
#     address = ("Абрикосовая", 23, 45)  # кортеж
#
#     data = {"header": header, "langs": langs, "user": user, "address": address}
#     return render(request, "index.html", context=data)


