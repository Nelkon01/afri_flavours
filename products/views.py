from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Product, Category, Allergen, Review


# Create your views here.

def all_products(request):
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    return render(request)
