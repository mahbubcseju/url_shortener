from django.db import models

# Create your models here.
class StoreUrl(models.Model):
    given_url = models.CharField(max_length=1000)
