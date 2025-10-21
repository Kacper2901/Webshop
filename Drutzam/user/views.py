from django.shortcuts import render
from django.http import HttpResponse


def info(request):
    return HttpResponse("Soon here will be information about user")