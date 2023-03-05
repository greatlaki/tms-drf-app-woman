from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({"posts": list(lst)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            category_id=request.data["category_id"],
        )
        return Response({"post": model_to_dict(post_new)})


class WomenListAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
