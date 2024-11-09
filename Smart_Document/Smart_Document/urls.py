from django.contrib import admin
from django.urls import path, include
from vege.views import receipes


urlpatterns = [
    path(
        'admin/',
        admin.site.urls
    ),
    path('recipes/', receipes, name="home")
    # path(
    #     'document/',
    #     include('Document.urls')
    # )
]
