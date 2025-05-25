from rest_framework.routers import DefaultRouter
from django.urls import path, include
from Document.api.views import (
    DepatmentListCreateAPIView,
    TemplateListCreateAPIView,
    PositionListCreateAPIView,
    UniversityListCreateAPIView,
)


router = DefaultRouter()


urlpatterns = [

    # path('v1/enlistment/', include("Document.api.urls")),
    path(
        'v1/depatment/',
        DepatmentListCreateAPIView.as_view(),
        name='depatment_api'
    ),
    path(
        'v1/template/',
        TemplateListCreateAPIView.as_view(),
        name='template_api'
    ),
    path(
        'v1/position/',
        PositionListCreateAPIView.as_view(),
        name='position_api'
    ),
    path(
        'v1/university/',
        UniversityListCreateAPIView.as_view(),
        name='university_api'
    ),


    # router ------------------------------------------------------------------
    path('', include(router.urls)),
]