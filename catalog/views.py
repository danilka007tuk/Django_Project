from django.http import HttpResponse
from django.shortcuts import render

#Создание контроллеров на приложение catalog

def sfera(request):
    """Контроллер отвечающий за маршрутизацию главной страницы"""
    return render(request, 'catalog/home.html')


def contact(request):
    """Контроллер отвечающий за маршрутизацию Контактной страницы"""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"\nПолучена форма: {name}, {phone}, {message}\n")
        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено.')
    return render(request, 'catalog/contacts.html')