from django.shortcuts import render, get_object_or_404, redirect
from .form import OrderUploadForm
from .models import Order

def upload_orders(request):
    form = OrderUploadForm()

    if request.method == "POST":
        form = OrderUploadForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "orders/orders_upload.html", {"form": form})

def orders_list(request):
    orders =  Order.objects.all()
    return render(request, "orders/orders_list.html", {"orders": orders})

def orders_detail(request, id):
    orders = get_object_or_404( Order, id=id)
    return render(request, "orders/orders_detail.html", {"orders": orders})

def edit_orders_view(request, id):
    orders = get_object_or_404( Order, id=id)

    if request.method == "POST":
        form =  OrderUploadForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect("orders_detail", id=orders.id)
    else:
        form =  OrderUploadForm(instance=orders)

    return render(request, "orders/edit_orders.html", {"form": form})


