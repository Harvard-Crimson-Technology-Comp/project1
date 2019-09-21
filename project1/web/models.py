from django.db import models

class UserModel(models.Model):
    class Meta:
        app_label = 'web'

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)