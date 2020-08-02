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
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)        