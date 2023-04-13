from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

## import models
from jobdescription import serializers

# Create your views here.
from core.models import JobDescription
from rest_framework import viewsets


class JobDescriptionViewSet(viewsets.ModelViewSet):
    """Views for managing JobDescription apis"""

    serializer_class = serializers.JobDescriptionDetailSerializer
    queryset = JobDescription.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        We want to filter out JobDescription for authenticated users
        """

        return self.queryset.filter(user=self.request.user).order_by("-id")

    def get_serializer_class(self):
        """Returns the serializer class to be used for the request"""

        if self.action == "list":
            return serializers.JobDescriptionSerializer
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
