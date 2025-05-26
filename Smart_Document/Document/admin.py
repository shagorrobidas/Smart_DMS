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


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'location', )
    list_filter = ('name', 'code', 'location', )
    search_fields = ('name', 'code', 'location')
    ordering = ('name',)


admin.site.register(University, UniversityAdmin)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_name', 'program_code')
    list_filter = ('program_name', 'program_code')
    ordering = ('program_name',)
    search_fields = ('program_name',)


admin.site.register(Program, ProgramAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'short_name')
    list_filter = ('name', 'code', 'short_name')
    ordering = ('name',)
    list_editable = ('code', 'short_name')
    list_per_page = 10
    search_fields = ('name',)


admin.site.register(Department, DepartmentAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'position_code')
    search_fields = ('title',)


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'code')
    search_fields = ('title',)


# Register your models

admin.site.register(Student)
admin.site.register(Position, PositionAdmin)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Experiment)
admin.site.register(Submission)

