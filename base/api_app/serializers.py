from rest_framework import serializers
from base.models import list


class ListSerializer(serializers.ModelSerializer):
  class Meta:
    model=list
    fields=['id','body','complete']
