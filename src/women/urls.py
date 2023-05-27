from django.urls import path

# from women.views import WomenAPIView
from women.views import WomenDestroyAPIView, WomenListCreateAPIView, WomenUpdateAPIView

urlpatterns = [
    # path("posts/", WomenAPIView.as_view(), name="get-post-posts"),
    # path("posts/<int:pk>/", WomenAPIView.as_view(), name="update-posts"),
    path("", WomenListCreateAPIView.as_view(), name="get-create-posts"),
    path("<int:pk>/", WomenUpdateAPIView.as_view(), name="update-post"),
    path("delete/<int:pk>/", WomenDestroyAPIView.as_view(), name="delete-post"),
]
