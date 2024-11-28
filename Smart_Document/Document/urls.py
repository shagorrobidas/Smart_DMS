from django.urls import path
from .views import (
    SubmissionCreateView,
    AssignmentCoverPageView,
    LabCoverPageView,
    createFromView,
)

urlpatterns = [
    path(
        'submission/create_1/',
        SubmissionCreateView.as_view(),
        name='submission_create'
    ),
    path(
        'submission/assignment/',
        AssignmentCoverPageView.as_view(),
        name='submission_assignment'
        ),
    path(
        'submission/labreport/',
        LabCoverPageView.as_view(),
        name='submission_labreport'
        ),
    path(
        'submission/create/',
        createFromView.as_view(),
        name='assignment_create'
        ),

]
