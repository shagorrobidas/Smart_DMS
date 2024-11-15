# forms.py
from django import forms
from .models import Submission


class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = [
            'report_number',
            'submission_date',
            'student',
            'instructor',
            'course',
            'template',
            'experiment',
            'university'
        ]
