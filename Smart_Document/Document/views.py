# views.py
import logging
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .models import Submission
from .forms import SubmissionForm

logger = logging.getLogger(__name__)
from .models import University, Department, Position, Template


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


class CoverPageFormView(TemplateView):
    template_name = "create.html"

    def get_context_data(self, **kwargs):
        print("get_context_data")
        context = super().get_context_data(**kwargs)
        context['universities'] = University.objects.all()
        context['departments'] = Department.objects.all()
        context['positions'] = Position.objects.all()
        context['templates'] = Template.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        print("post")
        page_type = request.POST.get('page_type')
        print(f"Page Type: {page_type}")
        course_code = request.POST.get('course_code')
        print(f"Course Code: {course_code}")
        university_name = request.POST.get('university')
        print(f"University Name: {university_name}")
        logger.info(f"{'*' * 10} university_name {university_name}")

        if page_type == 'assignment':
            print("Assignment button clicked")
            
        elif page_type == 'labreport':
            print("Lab Report button clicked")
            

