from rest_framework import serializers

from .models import Email, Profile


class SubscriberSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return Email.objects.create(**validated_data)


class ProfileSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=300)
    fullname = serializers.CharField(max_length=300)
    birthDate = serializers.CharField(max_length=300)
    age = serializers.CharField(max_length=300)
    education = serializers.CharField(max_length=300)
    university = serializers.CharField(max_length=300)
    workplace = serializers.CharField(max_length=300)
    position = serializers.CharField(max_length=300)
    pic_url = serializers.CharField(max_length=300)
    facebook_url = serializers.CharField(max_length=300)
    instragram_url = serializers.CharField(max_length=300)
    github_url = serializers.CharField(max_length=300)

    def create(self, validated_data):
        return Profile.objects.create(**validated_data)
