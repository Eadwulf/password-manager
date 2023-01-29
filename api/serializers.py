from rest_framework import serializers

from accounts.models import User
from credentials.models import Credential
from websites.models import Website


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class CredentialSerializer(serializers.ModelSerializer):
    website = serializers.HyperlinkedRelatedField('website-detail', queryset=Website.objects.all())

    class Meta:
        model = Credential
        fields = ['id', 'username', 'password', 'website', 'added_on', 'last_modified']


class WebsiteSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField('user-detail', queryset=User.objects.all())

    class Meta:
        model = Website
        fields = ['id', 'url', 'name', 'description', 'user']
