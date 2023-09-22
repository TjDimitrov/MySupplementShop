from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from ExamProject.products.forms import ProductCreateForm, ProductEditForm, ProductDeleteForm
from ExamProject.products.models import Product, Rating, Cart


def get_user_rating(user_id):
    return Rating.objects.filter(user_id=user_id)


def products_page(request, category_name=None, brand_name=None):
    all_products = Product.objects.all()
    if category_name:
        all_products = Product.objects.filter(category__name=category_name)
    elif brand_name:
        all_products = Product.objects.filter(brand__name=brand_name)
    context = {
        'all_products': all_products,
    }
    return render(request, template_name='products/products-main.html', context=context)


def product_details_page(request, pk):
    product = Product.objects.filter(id=pk).first()
    total_scores = len(Rating.objects.filter(product=product))
    context = {
        'product': product,
        'total_scores': total_scores,
    }

    return render(request, template_name='products/product-details.html', context=context)


@login_required
def add_product(request):
    if request.method == 'GET':
        form = ProductCreateForm()
    else:
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {
        'form': form,
    }
    return render(request, 'products/product-add.html', context=context)


@login_required
def edit_product(request, pk):
    product = Product.objects.filter(id=pk).first()
    if request.method == 'GET':
        form = ProductEditForm(instance=product)
    else:
        form = ProductEditForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product details', pk)
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'products/product-edit.html', context=context)


@login_required
def delete_product(request, pk):
    product = Product.objects.filter(id=pk).first()
    form = ProductDeleteForm()
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request, 'products/product-delete.html', {'form': form, 'pk': pk})


@login_required
def rate(request: HttpRequest, product_id: int, rating: int) -> HttpResponse:
    product = Product.objects.get(pk=product_id)
    user = request.user
    Rating.objects.filter(product=product, user=user).delete()
    product.rating_set.create(user=request.user, score=rating)
    return product_details_page(request, user.id)


@login_required
def add_to_cart(request, product_id):
    if request.POST and request.POST.get('product_qty'):
        cycles = int(request.POST.get('product_qty'))
    else:
        cycles = 1
    for _ in range(cycles):
        product = get_object_or_404(Product, pk=product_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()

    return JsonResponse({})


@login_required
def remove_from_cart(request, product_id):
    cart_item = get_object_or_404(Cart, product_id=product_id, user=request.user)
    cart_item.delete()
    return redirect(view_cart)


@login_required
def view_cart(request, sort_type=None):
    cart_items = Cart.objects.filter(user=request.user)
    total_items = len(cart_items)
    total = sum(item.product.price * item.quantity for item in cart_items)
    if sort_type == 'quantity':
        cart_items = cart_items.order_by(sort_type)
    elif sort_type == 'name' or sort_type == 'price':
        cart_items = cart_items.order_by(f'product__{sort_type}')
    context = {
        'cart_items': cart_items,
        'total': total,
        'total_items': total_items
    }
    return render(request, 'products/cart.html', context=context)


