from django.urls import path
from . import views

urlpatterns = [
    path("feedbacks/upload/", views.upload_feedback, name="feedback_upload_view"),
    path("feedbacks/<int:id>/", views.feedback_detail, name="feedback_detail_view"),
    path("feedbacks/list/", views.feedback_list, name="feedback_list_view"),
    path("feedbacks/edit/<int:id>/", views.edit_feedback_view, name="feedbackr_edit_view"),
]

