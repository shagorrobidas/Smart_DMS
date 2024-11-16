from django.contrib import admin
from django.urls import path, include
from vege.views import receipes, delete_receipes
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Document.views import ListDocumentView


urlpatterns = [
    path(
        'manage/',
        admin.site.urls
    ),
    path('api/', include('API.urls')),

    path('recipes/', receipes, name="home"),
    path('delete-recipes/<id>', delete_receipes, name="delete_recipes"),
    path(
        'document/',
        include('Document.urls')
    ),
    path(
        '',
        ListDocumentView.as_view(),
        name='submission_create'
        ),

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()