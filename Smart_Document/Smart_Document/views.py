from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = "login.html"
# https://docs.djangoproject.com/en/5.1/ref/contrib/messages/#using-messages-in-views-and-templates


class RegistrationView(TemplateView):
    template_name = "registration.html"
