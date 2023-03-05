from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        return Response({"title": "Angelina Jolie"})


class WomenListAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
