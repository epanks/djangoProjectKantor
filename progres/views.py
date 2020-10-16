from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import PaketCreateForm


# from rest_framework import viewsets
# from rest_framework.response import Response
# from .serializers import *


def home(request):
    title = 'Welcome: This is the Home Page'
    form = 'Weslcome form'
    context = {
        "title": title,
        "test": form,
    }
    return render(request, "progres/home.html", context)


def list_balai(request):
    title = 'Daftar Paket'
    queryset = Balai.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
    }
    return render(request, "progres/list_balai.html", context)


# class PaketView(viewsets.ViewSet):
#     pagu_paket = Paket.objects.prefetch_related('pagu').all()
#     serializer = PaketSerializer(pagu_paket, many=True)
#     return Response(serializer.data)
#
# class PaguView(viewsets.ViewSet):
#     listpagu = Pagu.objects.prefetch_related('kecamatan').all()
#     serializer = PaguSerializer(listpagu, many=True)
#     return Response(serializer.data)

def list_paket(request):
    header = 'Daftar Paket'
    queryset = Paket.objects.all()
    context = {
        "header": header,
        "queryset": queryset,
    }
    return render(request, "progres/list_paket.html", context)


def add_paket(request):
    form = PaketCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('progres/list_paket')
    context = {
        "form": form,
        "title": "Add Paket",
    }
    return render(request, "progres/add_paket.html", context)
