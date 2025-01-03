from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    return HttpResponse("به فروشگاه آنلاین ما خوش آمدید!" "محصولی یافت نشد.")