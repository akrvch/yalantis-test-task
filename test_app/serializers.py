from rest_framework.serializers import ModelSerializer
from test_app.models import *


class DriverSerializer(ModelSerializer):
    """Driver model serializer."""
    class Meta:
        model = Driver
        fields = ["id", "first_name", "last_name", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class VehicleSerializer(ModelSerializer):
    """Vehicle model serializer."""
    class Meta:
        model = Vehicle
        fields = ["id", "driver", "make", "model", "plate_number", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]