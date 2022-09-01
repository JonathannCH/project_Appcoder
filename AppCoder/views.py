from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso

# Create your views here.

def curso(request):
    curso=Curso(nombre="python", comision=2021)
    curso2=Curso(nombre="Lenguaje", comision=2022)
    curso3=Curso(nombre="Mate", comision=2023)
    curso.save()
    curso2.save()
    curso3.save()
    texto=f"Cursos creados: "
    return HttpResponse (texto)

