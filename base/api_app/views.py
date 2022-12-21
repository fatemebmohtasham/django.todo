from . serializers import ListSerializer
from rest_framework import generics
from base.models import list
from rest_framework.response import Response


class ListGenerics(generics.ListCreateAPIView):
  queryset=list.objects.all()
  serializer_class=ListSerializer
  def get(self,request,*args,**kwargs):
    return self.list(request,*args,**kwargs)


class DetailsListGenerics(generics.RetrieveUpdateDestroyAPIView):
  queryset=list.objects.all()
  serializer_class=ListSerializer
