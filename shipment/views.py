from django.shortcuts import render, get_object_or_404, redirect
from .form import  ShipmentUploadForm
from .models import  Shipment

def upload_shipment(request):
    form =  ShipmentUploadForm()

    if request.method == "POST":
        form = ShipmentUploadForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "shipment/shipment_upload.html", {"form": form})

def shipment_list(request):
    shipment = Shipment.objects.all()
    return render(request, "shipment/shipment_list.html", {"shipment": shipment})

def shipment_detail(request, id):
    shipment = get_object_or_404(Shipment, id=id)
    return render(request, "shipment/shipment_detail.html", {"shipment": shipment})

def edit_shipment_view(request, id):
    shipment = get_object_or_404(Shipment, id=id)

    if request.method == "POST":
        form = ShipmentUploadForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect("shipment_detail", id=shipment.id)
    else:
        form = ShipmentUploadForm(instance=shipment)

    return render(request, "shipment/edit_shipment.html", {"form": form})



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
      

