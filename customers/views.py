from django.shortcuts import render,redirect,get_object_or_404
from .models import Customer
from .form import CustomerUploadForm

def upload_customer(request):
    form = CustomerUploadForm()

    if request.method == "POST":
        form = CustomerUploadForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "customers/customer_upload.html", {"form": form})

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, "customers/customer_detail.html", {"customer": customer})


def customer_list(request):
    customer = Customer.objects.all()
    return render(request, "customers/customer_list.html", {"customer": customer})

def edit_customer_view(request, id):
    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        form = CustomerUploadForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("product_detail", id=customer.id)
    else:
        form = CustomerUploadForm(instance=customer)

    return render(request, "customers/edit_customer.html", {"form": form})
