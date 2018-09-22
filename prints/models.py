from django.db import models

class Print(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    size = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(upload_to='img', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.title
    
