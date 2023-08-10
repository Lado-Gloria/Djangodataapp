from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from .forms import CartUploadForm

def upload_cart(request):
    form = CartUploadForm()

    if request.method == "POST":
        form = CartUploadForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "cart/cart_upload.html", {"form": form})
def cart_detail(request, id):
    cart = get_object_or_404(Cart, id=id)
    return render(request, "cart/cart_detail.html", {"cart": cart})


def cart_list(request):
    cart = Cart.objects.all()
    return render(request, "cart/cart_list.html", {"cart": cart})

def edit_cart_view(request, id):
    cart = get_object_or_404(Cart, id=id)

    if request.method == "POST":
        form = CartUploadForm(request.POST, instance=cart)
        if form.is_valid():
            form.save()
            return redirect("cart_detail", id=cart.id)
    else:
        form = CartUploadForm(instance=cart)

    return render(request, "cart/edit_cart.html", {"form": form})