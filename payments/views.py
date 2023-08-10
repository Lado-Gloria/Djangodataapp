from django.shortcuts import render, get_object_or_404, redirect
from .form import PaymentsUploadForm
from .models import Payments

def upload_payments(request):
    form = PaymentsUploadForm()

    if request.method == "POST":
        form = PaymentsUploadForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "payments/payments_upload.html", {"form": form})

def payments_list(request):
    payments = Payments.objects.all()
    return render(request, "payments/payments_list.html", {"payments": payments})

def payments_detail(request, id):
    payments= get_object_or_404(Payments, id=id)
    return render(request, "payments/payments_detail.html", {"payments": payments})

def edit_payments_view(request, id):
    payments= get_object_or_404(Payments, id=id)

    if request.method == "POST":
        form = PaymentsUploadForm(request.POST, instance=payments)
        if form.is_valid():
            form.save()
            return redirect("payments_detail", id=payments.id)
    else:
        form = PaymentsUploadForm(instance=payments)

    return render(request, "payments/edit_payments.html", {"form": form})



# def upload_product(request):
#    if request.method=="POST":
#      form=ProductUploadForm(request.POST,request.FILES)
#      if form.is_valid():
#         form.save()
#    else:
#        form =ProductUploadForm()
#    return render(request, "inventory/product_upload.html",{"form":form})

# def products_list(request):
#    products =Product.objects.all()
#    images = []
#    for product in products:
#         images.append(product.image)
#    return render(request,"inventory/product_list.html",{"products": products, "images": images})

# def products_detail(request,id):
#    product=Product.objects.get(pk=id)
#    return render(request,"inventory/product_detail.html",{"product":product})

#    product=Product.objects.get(id=id)
#    if request.method=="POST":
#       form =ProductUploadForm(request.POST,instance=product)
#       if form.is_valid():
#          form.save()
#          return redirect("product_detail_view",id=product.id)
#       else:
#          form=ProductUploadForm(instance=product)
#          return render(request,"inventory/edit_product.html",{"form":form})
      

