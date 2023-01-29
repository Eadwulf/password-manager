from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

from credentials.models import Credential
from .serializers import CredentialSerializer


@api_view(['GET', 'POST'])
def credential_list(request, format=None):
    if request.method == 'GET':
        serialized_credential = CredentialSerializer(Credential.objects.all(), many=True)
        return Response(serialized_credential.data, status=status.HTTP_200_OK)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def credential_detail(request, pk, format=None):
    try:
        credential_obj = Credential.objects.get(pk=pk)
    except Credential.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized_credential = CredentialSerializer(credential_obj)
        return Response(serialized_credential.data, status=status.HTTP_200_OK)

    if request.method == 'PUT' or request.method == 'PATCH':
        serialized_credential = CredentialSerializer(credential_obj, data=request.data)
        if serialized_credential.is_valid():
            serialized_credential.save()
            return Response(serialized_credential.data, status=status.HTTP_200_OK)
        return Response(serialized_credential.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        credential_obj.delete()
        return Response(status.HTTP_204_NO_CONTENT) 
    