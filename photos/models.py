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
    image_location = models.ForeignKey('Location',on_delete=models.CASCADE,)
    image_category = models.ForeignKey('Category',on_delete=models.CASCADE,)  

    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images

    @classmethod
    def filter_images_by_location(cls,id):
        images_by_location = cls.objects.filter(image_location_id = id) 
        return images_by_location 

    @classmethod
    def search_image(cls,category):
        photos = cls.objects.filter(image_category__name__icontains=category)
        return photos       
