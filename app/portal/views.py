from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

## import models
from portal import serializers

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from core.models import Portal
from rest_framework import viewsets
from rest_framework.views import APIView


class PortalViewSet(viewsets.ModelViewSet):
    """Views for managing portal apis"""

    serializer_class = serializers.PortalDetailSerializer
    queryset = Portal.objects.all()
    # In order to use endpoint provided by this viewset, we will need ]
    # authentication
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def get(self, request, format=None):
    #     """
    #     Return a list of all portal.
    #     """
    #     portal = [portal for portal in Portal.objects.all()]
    #     return Response(portal)

    # If we are not used below function we can easily used crud operation
    def get_queryset(self):
        """
        We want to filter out jobtitles for authenticated users
        """

        return self.queryset.filter(user=self.request.user).order_by("-id")

    def get_serializer_class(self):
        """Returns the serializer class to be used for the request"""

        if self.action == "list":
            return serializers.PortalSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new job title
        # TODO - refer
        https://www.django-rest-framework.org/api-guide/generic-views/#methods
        Args:
            serializer: validated serializer
        Returns:
        """

        serializer.save(user=self.request.user)


# API views for crud operation using
# https://github.com/SurajT22/rest_api-crud-oprtaions-/blob/master/api_basic/views.py
# class PortalViewSetCRUD(APIView):
#     def get_object(self, id):
#         try:
#             return Portal.objects.get(id=id)
#         except Portal.DoesNotExists:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, id):
#         article = self.get_object(id)
#         serializer = PortalSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         article = self.get_object(id)
#         serializer = PortalSerializer(article, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
