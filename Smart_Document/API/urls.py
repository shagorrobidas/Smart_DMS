from rest_framework.routers import DefaultRouter
from django.urls import path, include
from Document.api.views.depatment_views import DepatmentListCreateAPIView

router = DefaultRouter()


urlpatterns = [

    # path('v1/enlistment/', include("Document.api.urls")),
    path(
        'v1/depatment/',
        DepatmentListCreateAPIView.as_view(),
        name='depatment_api'
        ),


    # router ------------------------------------------------------------------
    path('', include(router.urls)),
]