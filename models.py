from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
  
#  User = models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
 User = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,
                             limit_choices_to={'is_staff':True})
 page_name = models.CharField(max_length=100)
 page_categry = models.CharField(max_length=100)
 page_publish_date = models.DateField() 