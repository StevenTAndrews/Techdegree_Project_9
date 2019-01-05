from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import *
from .forms import *


def menu_list(request):
    menus = Menu.objects.all().prefetch_related('items')
    return render(request, 'menu/list_all_current_menus.html', {'menus': menus})


def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})


def item_detail(request, pk):
    item = get_object_or_404(Item.objects.select_related(), pk=pk)
    return render(request, 'menu/detail_item.html', {'item': item})


def create_new_menu(request):
    form = MenuForm()
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save()
            return redirect('menu_detail', pk=menu.pk)
    return render(request, 'menu/menu_edit.html', {'form': form})


def edit_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    items = Item.objects.all()
    form = MenuForm(instance=menu)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save()
            return redirect('menu_detail', pk=menu.pk)
    return render(request, 'menu/menu_edit.html', {
        'menu': menu,
        'form': form, })
