from django.contrib import admin
from .models import (
    University,
    Student,
    Program,
    Department,
    Position,
    Instructor,
    Course,
    Template,
    Experiment,
    Submission
)

# Register your models here.
admin.site.register(University)
admin.site.register(Student)
admin.site.register(Program)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Template)
admin.site.register(Experiment)
admin.site.register(Submission)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'program_code')
    search_fields = ('program_name',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department_code')
    search_fields = ('name',)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'position_code')
    search_fields = ('title',)


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')
    search_fields = ('title',)
