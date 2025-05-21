from django.shortcuts import render

#Создание контроллеров на приложение catalog

def sfera(request):
    return render(request, 'catalog', name='catalog')