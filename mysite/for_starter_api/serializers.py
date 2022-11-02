from .models import *
from rest_framework import serializers


class ManagerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager_Account
        fields = '__all__'


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'


class SoftwareUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'
