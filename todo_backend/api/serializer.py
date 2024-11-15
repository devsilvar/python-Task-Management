from rest_framework.serializers import ModelSerializer
from .models import todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = todo
        fields = "__all__"