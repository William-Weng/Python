from django.http import HttpResponse
from django import template
from django.template.loader import get_template
from django.shortcuts import render_to_response

def here(response):
    return HttpResponse('我在這裡')

def add(response, num1, num2):
    ans = int(num1) + int(num2)
    return HttpResponse(str(ans))

def temp(response):
    text = {'name':'William-Weng','djangoVersion':'1.9.5'}
    return render_to_response('main.html', locals())
