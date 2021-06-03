from rest_framework import serializers

from .models import Client,Project


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id','clientName','clientCountry']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id','projectName','projectLanguage','projectClient']