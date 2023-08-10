from django.shortcuts import render,redirect,get_object_or_404
from .models import Feedback
from .form import FeedbackUploadForm

def upload_feedback(request):
    form = FeedbackUploadForm()

    if request.method == "POST":
        form = FeedbackUploadForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, "feedback/feedback_upload.html", {"form": form})

def feedback_detail(request, id):
    feedback= get_object_or_404(Feedback, id=id)
    return render(request, "feedback/feedback_detail.html", {"feedback": feedback})


def feedback_list(request):
    feedback = Feedback.objects.all()
    return render(request, "feedback/feedback_list.html", {"feedback": feedback})

def edit_feedback_view(request, id):
    feedback = get_object_or_404(Feedback, id=id)

    if request.method == "POST":
        form = FeedbackUploadForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect("feedback_detail", id=feedback.id)
    else:
        form = FeedbackUploadForm(instance=feedback)

    return render(request, "feedback/edit_feedback.html", {"form": form})
