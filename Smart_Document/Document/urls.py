from django.urls import path
from .views import (
    SubmissionCreateView,
    CoverPageView,
    createFromView
)

urlpatterns = [
    path(
        'submission/create_1/',
        SubmissionCreateView.as_view(),
        name='submission_create'
    ),
    path(
        'submission/coverpage/',
        CoverPageView.as_view(),
        name='submission_create'
        ),
    path(
        'submission/create/',
        createFromView.as_view(),
        name='assignment_create'
        ),

]
