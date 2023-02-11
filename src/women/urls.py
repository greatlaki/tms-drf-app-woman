from django.urls import path
from women.views import WomenListAPIView


urlpatterns = [
    path("", WomenListAPIView.as_view(), )
]
