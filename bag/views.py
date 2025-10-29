from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)

from django.contrib import messages
from products.models import Product

import logging

logger = logging.getLogger(__name__)


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a quantity of the specified product to the shopping bag.

    If the product already exists in the bag, increases the quantity.
    Otherwise, adds the product with the specified quantity.

    Args:
        item_id: The ID of the product to add to the bag.

    Returns:
        Redirects to the URL specified in the POST data.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """
    Adjust the quantity of a product in the shopping bag.

    If quantity is greater than 0, updates the quantity.
    If quantity is 0, removes the product from the bag.

    Args:
        item_id: The ID of the product to adjust.

    Returns:
        Redirects to the bag view page.
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """
    Remove an item from the shopping bag.

    Args:
        item_id: The ID of the product to remove from the bag.

    Returns:
        HttpResponse with status 200 on success, 500 on error.
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        logger.error(f'Error removing item {item_id} from bag: {e}', exc_info=True)
        messages.error(request, 'Error removing item from your bag. Please try again.')
        return HttpResponse(status=500)
