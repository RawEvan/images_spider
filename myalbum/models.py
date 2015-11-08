from django.db import models

# Create your models here.
class ImgStorage(models.Model):
    originalUrl = models.CharField(max_length = 200, unique = True)
    storageUrl = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.originalUrl
