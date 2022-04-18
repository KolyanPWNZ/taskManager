from rest_framework import serializers
from .models import Task, Post


class TaskSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description']


class PostSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'posted']
