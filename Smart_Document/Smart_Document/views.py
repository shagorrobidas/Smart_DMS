# https://docs.djangoproject.com/en/5.1/ref/contrib/messages/#using-messages-in-views-and-templates
# from django.shortcuts import redirect, render
from django.views.generic import (
    TemplateView,
    FormView
)
from django.contrib.auth.forms import UserCreationForm


class LoginView(TemplateView):
    template_name = "login.html"


class RegistrationView(FormView):
    template_name = "registration.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# view, view.grnatics, view.api view , view,viewset , modelviewset, query
