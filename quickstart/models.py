from django.conf import settings
from django.db import models
from django.utils import timezone

FILES_DIR = getattr(settings, 'FILES_DIR', 'files')

class File(models.Model):
    name = models.CharField(max_length=200)
    data = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(default=timezone.now)
    objects = models.Manager()

    @staticmethod
    def get(name):
        file = open(FILES_DIR + "/" + name, 'rb').read()
        return file

    def __unicode__(self):
        return self.name
