# views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Submission
from .forms import SubmissionForm


class SubmissionCreateView(CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = 'document/create_submission.html'
    success_url = reverse_lazy('submission_list')  # Redirect to submission list page after saving #noqa
