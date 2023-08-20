from django.db import models
from cloudinary.models import CloudinaryField

class FileUpload(models.Model):
    user = models.CharField(max_length=50)
    activity = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image')

        
# Create your models here.
