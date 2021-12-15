from django.db import models

# Create your models here.


class Post(models.Model):
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255,default="kkupload")
    photo = models.ImageField(null=False, blank=False,
                              upload_to='static/image')

    def __str__(self):
        return self.name
