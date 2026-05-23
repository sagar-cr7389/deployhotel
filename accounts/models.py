from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    price = models.IntegerField()
    email = models.EmailField()
    image = models.ImageField(upload_to='hotel_images/')

    def __str__(self):
        return self.name