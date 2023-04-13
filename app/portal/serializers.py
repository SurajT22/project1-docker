"""
Serializers for Portal APIs
"""


from rest_framework import serializers
from core.models import Portal


class PortalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portal
        fields = ["name", "description"]
        read_only_fields = ["id"]


class PortalDetailSerializer(serializers.ModelSerializer):
    class Meta(PortalSerializer.Meta):
        fields = PortalSerializer.Meta.fields + [
            "user",
        ]
