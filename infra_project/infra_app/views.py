from django.http import HttpResponse


def index(request):
    return HttpResponse.status_code('У меня получилось!')


def second_page(request):
    return HttpResponse.status_code('А это вторая страница')
