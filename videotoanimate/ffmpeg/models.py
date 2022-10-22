from distutils.command.upload import upload
from django.db import models

# Create your models here.
class VideoFile(models.Model):
    file = models.FileField(upload_to = "uploads/")