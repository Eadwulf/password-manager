from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

from credentials.models import Credential
from .serializers import CredentialSerializer


@api_view(['GET', 'POST'])
def credential_list(request):
    if request.method == 'GET':
        serialized_credential = CredentialSerializer(Credential.objects.all(), many=True)
        return Response(serialized_credential.data, status=status.HTTP_200_OK)
    

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def credential_detail(request, pk):
    if request.method == 'GET':
        try:
            serialized_credential = CredentialSerializer(Credential.objects.get(pk=pk))
            return Response(serialized_credential.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'msg': f'not matching object found for pk={pk}'}, status=status.HTTP_404_NOT_FOUND)