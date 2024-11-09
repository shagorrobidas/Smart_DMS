from django.urls import path
from .views import SubmissionCreateView

urlpatterns = [
    path(
        'submission/create/',
        SubmissionCreateView.as_view(),
        name='submission_create'
        ),
    

]
