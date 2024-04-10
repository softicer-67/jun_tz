from django.shortcuts import render
from .models import MenuItem


def home(request):
    main_menu = MenuItem.objects.filter(title="main_menu").first()
    return render(request, 'base.html', {'main_menu': main_menu})

