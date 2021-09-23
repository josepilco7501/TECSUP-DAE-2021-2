from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Desde la vista calculadora!")


def sumar(request,n1,n2):
    resultado=n1+n2
    responsive=("La suma de ",n1 ,"+" ,n2 ," es : ",resultado)
    return HttpResponse(responsive)

def restar(request,n1,n2):
    resultado=n1-n2 
    responsive=("La resta de ",n1 ,"-" ,n2 ," es : ",resultado)
    return HttpResponse(responsive)

def multiplicar(request,n1,n2):
    resultado=n1*n2 
    responsive=("El producto de ",n1 ,"*" ,n2 ," es : ",resultado)
    return HttpResponse(responsive)

def dividir(request,n1,n2):
    resultado=n1/n2 
    responsive=("El cociente de ",n1 ,"/" ,n2 ," es : ",resultado)
    return HttpResponse(responsive)

