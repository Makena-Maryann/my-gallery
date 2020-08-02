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