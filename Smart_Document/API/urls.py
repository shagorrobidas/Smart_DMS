from rest_framework.routers import DefaultRouter
from django.urls import path, include
from Document.api.views.depatment_views import DepatmentListView

router = DefaultRouter()


urlpatterns = [

    # path('v1/enlistment/', include("Document.api.urls")),
    path(
        'v1/depatment/',
        DepatmentListView.as_view(),
        name='depatment_api'
        ),


    # router ------------------------------------------------------------------
    path('', include(router.urls)),
]