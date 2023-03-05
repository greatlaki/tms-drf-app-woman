from django.urls import path

from women.views import WomenAPIView, WomenListAPIView

urlpatterns = [
    path("posts/", WomenAPIView.as_view(), name="get-post-posts"),
    path("posts/<int:pk>/", WomenAPIView.as_view(), name="update-posts"),
    path(
        "",
        WomenListAPIView.as_view(),
    ),
]
