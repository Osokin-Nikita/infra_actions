from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
#Проверка изменений - докерхаб
#Проверка изменений - ВМ