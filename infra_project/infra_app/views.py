from django.http import HttpResponse


def index(request):
    return HttpResponse('Похоже скоро 19 спринт пройду!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
