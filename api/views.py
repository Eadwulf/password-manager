from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from credentials.models import Credential
from websites.models import Website

from .serializers import CredentialSerializer, WebsiteSerializer


class GetObjectixin:

    def get_obj(self, model_class, pk):
        try:
            return model_class.objects.get(pk=pk)
        except model_class.DoesNotExist:
            return None
    
    def get_obj_list(self, model_class, *args, **kwargs):
        return model_class.objects.all()


class ListViewMixin(GetObjectixin, APIView):
    model_class = None
    serializer_class = None

    def get(self, request):
        serialized_data = self.serializer_class(self.get_obj_list(model_class=self.model_class), many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serialized_data = self.serializer_class(self.model_class, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serialized_data.erros, status=status.HTTP_400_BAD_REQUEST)


class DetailViewMixin(GetObjectixin, APIView):
    model_class = None
    serializer_class = None

    def get(self, request, pk):
        model_obj = self.get_obj(model_class=self.model_class, pk=pk)
        if model_obj:
            serialized_data = self.serializer_class(model_obj)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        model_obj = self.get_obj(model_class=self.model_class, pk=pk)
        if model_obj:
            serialized_data = self.serializer_class(self.model_class, data=request.data)
            if serialized_data.is_valid(): 
                serialized_data.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def path(self, request, pk):
        # later implementation
        pass

    def delete(self, request, pk):
        model_obj = self.get_obj(model_class=self.model_class, pk=pk)
        if model_obj:
            model_obj.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


class CredentialListView(ListViewMixin):
    model_class = Credential
    serializer_class = CredentialSerializer
    

class CredentialDetailView(DetailViewMixin, APIView):
    model_class = Credential
    serializer_class = CredentialSerializer
        

class WebsiteListView(ListViewMixin, APIView):
    model_class = Website
    serializer_class = WebsiteSerializer
    

class WebsiteDetailView(DetailViewMixin, APIView):
    model_class = Website
    serializer_class = WebsiteSerializer
