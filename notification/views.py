from django.shortcuts import render, get_object_or_404, redirect
from .form import NotificationUploadForm
from .models import Notification

def upload_notification(request):
    form = NotificationUploadForm()

    if request.method == "POST":
        form = NotificationUploadForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "notification/notification_upload.html", {"form": form})

def notification_list(request):
    notification = Notification.objects.all()
    return render(request, "notification/notification_list.html", {"notification": notification})

def notification_detail(request, id):
    notification = get_object_or_404(Notification, id=id)
    return render(request, "notification/notification_detail.html", {"notification": notification})

def edit_notification_view(request, id):
    notification = get_object_or_404(Notification, id=id)

    if request.method == "POST":
        form = NotificationUploadForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return redirect("notification_detail", id=notification.id)
    else:
        form = NotificationUploadForm(instance=notification)

    return render(request, "notification/edit_notification.html", {"form": form})

