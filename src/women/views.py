from women.serializers import WomenSerializer
from rest_framework import generics
from women.models import Women


class WomenListAPIView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
