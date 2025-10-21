from django.shortcuts import render
from django.http import HttpResponse

def info(HttpRequest):
    return HttpResponse("Here there will be a home page")
