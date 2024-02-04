import logging
from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice
import lorem


LOGGER = logging.getLogger(__name__)


def index(request):
    text = lorem.text()
    LOGGER.info('Переход на Главную страницу')
    return HttpResponse(f'<h1>Главная</h1>\n , {text}')


def about(rquest):
    text = lorem.text()
    LOGGER.info('Переход на страницу "Обо мне"')
    return HttpResponse(f'<h1>Обо мне</h1>\n , {text}')
# Create your views here.
