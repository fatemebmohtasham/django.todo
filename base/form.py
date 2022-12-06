from django.forms import ModelForm
from.models import list

class listform(ModelForm):
  class Meta:
    model=list
    fields=['body','complete']
