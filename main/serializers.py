from rest_framework import serializers
from .models import Task


class TaskSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description']
