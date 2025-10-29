from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProductForm
from .models import Product, Category, Review

from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView


def all_products(request):
    """A view to show all products, including sorting and search queries"""
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # Handling sorting
        sortkey = request.GET.get('sort')
        direction = request.GET.get('direction', '')

        if sortkey:
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey in ['category', 'allergens']:
                sortkey = f'{sortkey}__name'

            if direction == 'desc':
                sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # Handling category filtering
        categories = request.GET.get('category')
        if categories:
            category_list = categories.split(',')
            products = products.filter(category__name__in=category_list)
            categories = Category.objects.filter(name__in=category_list)

        # Handling search queries
        query = request.GET.get('q')
        if query:
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
        elif 'q' in request.GET:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': f'{sort}_{direction}',
        'all_categories': Category.objects.all(),
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view to show individual product details"""
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)

    context = {
        'product': product,
        'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a new product to the store.

    Requires superuser authentication. Handles both GET (display form)
    and POST (process form submission) requests.

    Returns:
        Redirects to product detail page on success,
        or renders add_product template with form on GET/failure.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {'form': form})


@login_required
def edit_product(request, product_id):
    """
    Edit an existing product in the store.

    Requires superuser authentication. Handles both GET (display form with
    existing data) and POST (process form updates) requests.

    Args:
        product_id: The ID of the product to edit.

    Returns:
        Redirects to product detail page on success,
        or renders edit_product template with form.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, f'Failed to update {product.name}. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


# Generic delete view for handling confirmation
class ProductDeleteView(DeleteView):
    """
    Handle product deletion with confirmation.

    Requires superuser authentication. Displays confirmation page
    before deleting the product from the database.

    Attributes:
        model: Product model class
        template_name: Template for deletion confirmation
        success_url: Redirect to products list after successful deletion
    """
    model = Product
    template_name = 'products/confirm_delete.html'
    success_url = reverse_lazy('products')

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect('home')
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, 'Sorry, only store owners can do that.')
            return redirect('home')
        messages.success(request, 'Product deleted!')
        return super().delete(request, *args, **kwargs)
