from django.db import models
from django.contrib.auth import get_user_model
import json
# Create your models here.

class FormShape(models.Model):
    item = models.CharField(max_length=600)
    type = models.CharField(max_length=600)
    options = models.CharField(max_length=600)
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def set_options(self,arr):
        self.options = json.dumps(arr)
    
    def get_options(self):
        self.options = json.loads(self.options)

    def __str__(self):
        return self.item
