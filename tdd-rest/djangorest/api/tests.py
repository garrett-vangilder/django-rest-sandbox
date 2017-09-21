from django.test import TestCase
from .models import Bucketlist


class ModelTestCase(TestCase):
    """This class defines the test suite for the bucketlist model."""

    def setUp(self):
        """Define the test client and other test variables"""
        self.bucketlist_name = "Write world class code"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_can_create_bucketlist(self):
        """Test the bucketlist model can create a bucketlist"""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertGreater(new_count, old_count)
