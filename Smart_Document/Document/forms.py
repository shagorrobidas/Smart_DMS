# forms.py
from django import forms
from .models import (
    Submission,
    University,
    Department,
    Position,
    Program
)


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


class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = [
            'name',
            'logo',
            'code',
            'location',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter university name'
            }),
            'logo': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter unique code (e.g., U123)'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter location'
            }),
        }

        def clean_logo(self):
            logo = self.cleaned_data.get('logo', False)
            if logo:
                if logo.size > 2*1024*1024:  # 2MB limit
                    raise forms.ValidationError(
                        "Image file too large ( > 2MB )")
                if not logo.content_type.startswith('image'):
                    raise forms.ValidationError("File is not an image")
            return logo


class DepatmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = [
            'name',
            'code',
            'short_name'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter department name'
            }),
            'code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter unique code (e.g., CS101)'
            }),
            'short_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter short name (e.g., CS)'
            }),
        }


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = [
            'title',
            'position_code',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter position name'
            }),
            'position_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter unique code (e.g., P001)'
            }),
        }


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = [
            'program_name',
            'program_code',
            'program_discription'
        ]
        widgets = {
            'program_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter program name'
            }),
            'program_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter unique code (e.g., BSc101)'
            }),
            'program_discription': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter program description',
                'rows': 3
            }),
        }

