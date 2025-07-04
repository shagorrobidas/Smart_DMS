from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import (
    SubmissionCreateView,
    AssignmentCoverPageView,
    LabCoverPageView,
    CoverPageFormView,
    UniversityTemplateView
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
        'submission/',
        CoverPageFormView.as_view(),
        name='coverpage_create'
    ),
    path(
        'university-list/',
        UniversityTemplateView.as_view(),
        name='university_List'
    ),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
