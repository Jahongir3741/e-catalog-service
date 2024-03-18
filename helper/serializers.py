from rest_framework import serializers
from .models import Serial


class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = "__all__"
        extra_kwargs = {
            "created": {"read_only": True},
            "updated": {"read_only": True}

        }



