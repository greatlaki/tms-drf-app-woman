from django.urls import path

from women.views import WomenAPIView, WomenListAPIView

urlpatterns = [
    path("apiview/", WomenAPIView.as_view(), name="base-view-class"),
    path(
        "",
        WomenListAPIView.as_view(),
    ),
]
