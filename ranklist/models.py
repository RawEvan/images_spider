from django.db import models

# Create your models here.

class person(models.Model):
    name = models.CharField(max_length = 50, unique = 'True')
    rank = models.IntegerField()

    def __unicode__(self):
        return 'name: %s    rank: %d' % (self.name, self.rank)
