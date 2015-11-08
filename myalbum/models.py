from django.db import models

# Create your models here.
class ImgStorage(models.Model):
    original_url = models.CharField(max_length = 200, unique = True)
    storage_url = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.original_url
