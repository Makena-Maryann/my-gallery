from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()    

    class Meta:
        ordering = ['name']  

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()        

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=40)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)                  