from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.nairobi=Location(name = 'Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    def test_save_method(self):
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)  

class CategoryTestClass(TestCase):
    def setUp(self):
        self.food = Category(name = 'Food')

    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))

    def test_save_method(self):
        self.food.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)                      

class ImageTestClass(TestCase):
    def setUp(self):
        self.nairobi=Location(name='Nairobi')
        self.nairobi.save_location()

        self.food=Category(name='Food')
        self.food.save_category()

        self.new_image=Image(image_name='Banner',image_description='A test image',image_location=self.nairobi,image_category=self.food)
        self.new_image.save()

    def tearDown(self):  
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()  

    def test_get_all_images(self):
        all_images = Image.get_images()
        self.assertTrue(len(all_images)>0)  

    def test_filter_images_by_location(self):
        test_location_id = 4
        images_by_location = Image.filter_images_by_location(test_location_id)
        self.assertTrue(len(images_by_location) == 0)      