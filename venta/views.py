
from .models import Venta
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json
# Create your views here.

def VentasList(request):
    queryset = Venta.objects.all()
    context = list(queryset.values('id', 'idVenta', 'producto', 'cantidad', 'total'))
    return JsonResponse(context, safe=False)

def VentaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        venta = Venta()
        venta.idVenta = data_json['idVenta']
        venta.producto = data_json['producto']
        venta.cantidad = data_json['cantidad']
        venta.total = data_json['total']
        venta.save()
        return HttpResponse("sucefully created venta")