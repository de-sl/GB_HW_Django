import logging
from django.shortcuts import render
from django.http import HttpResponse
from random import randint, choice



LOGGER = logging.getLogger(__name__)

def log(view):
    def wrapper(request, *args, **kwargs):
        res = view(request, *args,**kwargs)
        LOGGER.info(f'The function {view.__name__} was returned {res}')
        return res
    return wrapper
@log
def coin(request):
    i = randint(0, 1)
    """
    функция подбрасывает монету
    
    """
    if i == 0:
        LOGGER.info(f'Орел')
        return HttpResponse('Орёл')
    LOGGER.info(f'Решка')
    return HttpResponse('Решка')

@log
def dice(request):
    """
    функция подбрасывает шестигранный куб

    """
    i = randint(1,6)
    LOGGER.info(f'Выпало {i}')
    return HttpResponse(f'Выпало {i}')

@log
def rand_num(request):
    """
    функция выбирает случайное число от 0 до 100

    """
    i = randint(0, 101)
    LOGGER.info(f'Выпало {i}')
    return HttpResponse(f'Выпало {i}')
