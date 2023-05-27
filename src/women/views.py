from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from women.models import Women
from women.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from women.serializers import WomenSerializer

# class WomenAPIView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({"posts": WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = get_object_or_404(Women, pk=pk)
#         except Women.DoesNotExist:
#             raise Http404("Given query not found....")
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         try:
#             instance = get_object_or_404(Women, pk=pk)
#             instance.delete()
#         except Women.DoesNotExist:
#             raise Http404("Given query not found....")
#
#         return Response({"post": "delete post " + str(pk)})


class WomenListCreateAPIView(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenUpdateAPIView(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class WomenDestroyAPIView(generics.DestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)
