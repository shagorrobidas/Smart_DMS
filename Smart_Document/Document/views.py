# views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .models import Submission
from .forms import SubmissionForm


class SubmissionCreateView(CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = 'document/create_submission.html'
    success_url = reverse_lazy('submission_list')


class ListDocumentView(TemplateView):
    template_name = "home.html"
    

class AssignmentCoverPageView(TemplateView):
    template_name = "assignment_report.html"


class LabCoverPageView(TemplateView):
    template_name = "labreport_cover.html"


class createFromView(TemplateView):
    template_name = "create.html"
