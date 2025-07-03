# views.py
import logging
from django.urls import reverse_lazy
from django.shortcuts import render
from Smart_Document.utils import render_to_pdf

from django.http import HttpResponse
from django.views.generic import CreateView, TemplateView

from .forms import (
    SubmissionForm,
    UniversityForm,
    DepatmentForm,
    PositionForm
)
from .models import (
    University,
    Department,
    Position,
    Template,
    Submission,
    Program
)


logger = logging.getLogger(__name__)


class SubmissionCreateView(CreateView):
    model = Submission
    form_class = SubmissionForm
    template_name = 'document/create_submission.html'
    success_url = reverse_lazy('submission_list')


class ListDocumentView(TemplateView):
    template_name = "home.html"


class AssignmentCoverPageView(TemplateView):
    # template_name = "assignment_report.html"
    template_name = "assignment.html"
    

    def post(self, request, *args, **kwargs):
        context = {
            'course_code': request.POST.get('course_code', ''),
            'course_title': request.POST.get('course_title', ''),
            'assignment_no': request.POST.get('assignment_no', ''),
            'university': University.objects.filter(
                id=request.POST.get('university')
            ).first(),
            'teacher_name': request.POST.get('teacher_name', ''),
            'faculty_department': Department.objects.filter(
                id=request.POST.get('faculty_department')
            ).first(),
            'faculty_position': Position.objects.filter(
                id=request.POST.get('faculty_position')
            ).first(),
            'student_name': request.POST.get('student_name', ''),
            'student_id': request.POST.get('student_id', ''),
            'intake': request.POST.get('intake', ''),
            'program': Program.objects.filter(
                id=request.POST.get('student_program')
            ).first(),
            'section': request.POST.get('section', ''),
            'student_department': Department.objects.filter(
                id=request.POST.get('student_department')
            ).first(),
            'date': request.POST.get('date', ''),
        }

        action = request.POST.get('action')
        print(f"Received action: {action}")
        if action == 'preview_assignment':
            return render_to_pdf(self.template_name, context, download=False)
        elif action == 'download_assignment':
            return render_to_pdf(self.template_name, context, download=True)
        else:
            return HttpResponse("Invalid action", status=400)


class LabCoverPageView(TemplateView):
    template_name = "labreport_cover.html"

    def post(self, request, *args, **kwargs):
        context = {
            'course_code': request.POST.get('course_code', ''),
            'course_title': request.POST.get('course_title', ''),
            'labreport_name': request.POST.get('labreport_name', ''),
            'labreport_experiment': request.POST.get(
                'labreport_experiment', ''
            ),
            'university': University.objects.filter(
                id=request.POST.get('university')
            ).first(),
            'teacher_name': request.POST.get('teacher_name', ''),
            'faculty_department': Department.objects.filter(
                id=request.POST.get('faculty_department')
            ).first(),
            'faculty_position': Position.objects.filter(
                id=request.POST.get('faculty_position')
            ).first(),
            'student_name': request.POST.get('student_name', ''),
            'student_id': request.POST.get('student_id', ''),
            'intake': request.POST.get('intake', ''),
            'program': Program.objects.filter(
                id=request.POST.get('student_program')
            ).first(),
            
            'section': request.POST.get('section', ''),
            'student_department': Department.objects.filter(
                id=request.POST.get('student_department')
            ).first(),
            'date': request.POST.get('date', ''),
        }
        action = request.POST.get('action')
        print(f"Received action: {action}")
        if action == 'preview_labreport':
            return render_to_pdf(self.template_name, context, download=False)
        elif action == 'download_labreport':
            return render_to_pdf(self.template_name, context, download=True)
        else:
            return HttpResponse("Invalid action", status=400)


class CoverPageFormView(TemplateView):
    template_name = "create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['universities'] = University.objects.all()
        context['departments'] = Department.objects.all()
        context['positions'] = Position.objects.all()
        context['templates'] = Template.objects.all()
        context['programs'] = Program.objects.all()
        context['university_form'] = UniversityForm()
        context['department_form'] = DepatmentForm()
        context['position_form'] = PositionForm()
        return context


class UniversityTemplateView(TemplateView):
    template_name = "list/university_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['universities'] = University.objects.all()
        return context
