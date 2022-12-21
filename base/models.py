from django.db import models

# Create your models here.

class list(models.Model):
  body=models.CharField(max_length=200,null=True,blank=True)
  complete = models.BooleanField(default=False)
  created=models.DateField(auto_now_add=True)
  update=models.DateField(auto_now=True)
  def __str__(self):
    return self.body