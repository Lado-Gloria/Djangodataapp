from django.shortcuts import render, get_object_or_404, redirect
from .form import VendorUploadForm  # Assuming your form is named 'VendorUploadForm'
from .models import Vendor

def upload_vendor(request):
    if request.method == "POST":
        form = VendorUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vendor_list")
    else:
        form = VendorUploadForm()

    return render(request, "vendor/vendor_upload.html", {"form": form})

def vendor_list(request):
    print("Vendor list view is called.")  # Add this line
    vendors = Vendor.objects.all()
    return render(request, "vendor/vendor_list.html", {"vendors": vendors})

def vendor_detail(request, id):
    vendor = get_object_or_404(Vendor, id=id)
    return render(request, "vendor/vendor_detail.html", {"vendor": vendor})

def edit_vendor_view(request, id):
    vendor = get_object_or_404(Vendor, id=id)

    if request.method == "POST":
        form = VendorUploadForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            return redirect("vendor_detail", id=vendor.id)  # Redirect to updated vendor detail
    else:
        form = VendorUploadForm(instance=vendor)

    return render(request, "vendor/edit_vendor.html", {"form": form})
