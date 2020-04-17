from django.contrib.auth import authenticate
from rest_framework import serializers
from issues.models import Issue


class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = '__all__'


class LoginSerializer(serializers.Serializer):

    username = serializers.SlugField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'],
                            password=attrs['password'])
        if not user:
            raise serializers.ValidationError('Incorrect username/password')
        return user
