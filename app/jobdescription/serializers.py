"""
Serializers for JobDescription APIs
"""

from rest_framework import serializers
from core.models import JobDescription


class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = ["id", "role"]
        read_only_fields = ["id"]


class JobDescriptionDetailSerializer(serializers.ModelSerializer):
    class Meta(JobDescriptionSerializer.Meta):
        fields = JobDescriptionSerializer.Meta.fields + [
            "description_text",
        ]
