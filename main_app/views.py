from django.shortcuts import render, redirect
from main_app import models


# Create your views here.


def index(request):
    return render(request, 'index.html')


def edit(request):
    tips = request.GET.get('tips')
    data = models.Person.objects.all()
    return render(request, 'edit.html', {'tips': tips, 'data': data})


def save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        models.Person.objects.create(name=name, address=address, phone=phone)
        return redirect('/edit?tips=Save Succeed!')


def remove(request):
    id = request.GET.get('id')
    models.Person.objects.filter(id=id).delete()
    return redirect('/edit?tips=Remove Succeed!')