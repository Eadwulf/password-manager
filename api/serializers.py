from rest_framework import serializers

from accounts.models import User
from credentials.models import Credential
from websites.models import Website


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'fist_name', 'last_name', 'email']


class CredentialSerializer(serializers.ModelSerializer):
    website = serializers.StringRelatedField()

    class Meta:
        model = Credential
        fields = ['id', 'username', 'password', 'website', 'added_on', 'last_modified']


class WebsiteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Website
        fields = ['url', 'name', 'description', 'user']
