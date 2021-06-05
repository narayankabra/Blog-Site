from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    writeup = models.CharField(max_length=20000,default='0000000')


    def __str__(self):
        return self.summary

    def __str__(self):
        return self.writeup
