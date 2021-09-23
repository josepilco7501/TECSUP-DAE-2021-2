from django.urls import path

from.import views

urlpatterns = [
    #ex: localhost:8080/app/
    path('', views.index, name='index'),
    #ex: localhost:8080/app/sumar/n1+n2/
    path('sumar/<int:n1>/<int:n2>', views.sumar, name='suma'),
    #ex: localhost:8080/app/sumar/n1-n2/
    path('restar/<int:n1>/<int:n2>', views.restar, name='resta'),
    #ex: localhost:8080/app/multiplicar/n1*n2/
    path('multiplicar/<int:n1>/<int:n2>', views.multiplicar, name='multiplicacion'),
    #ex: localhost:8080/app/multiplicar/n1/n2/
    path('dividir/<int:n1>/<int:n2>', views.dividir, name='division'),
    ]

