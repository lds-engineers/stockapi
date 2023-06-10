import uuid
from django.db import models
from django.contrib.auth.models import *
from datetime import date
# Create your models here.


class UniqueUserKey(models.Model):
    key = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = uuid.uuid4()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.key
    
    
    
class ActiveUser(models.Model):
    Api_Key = models.ForeignKey(UniqueUserKey, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        if self.created_date is None:
            self.created_date = date.today()
        super().save(*args, **kwargs)
    
    
    def __str__(self):
        return self.user.first_name
