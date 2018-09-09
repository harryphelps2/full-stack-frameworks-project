from django.test import TestCase
from .models import Prints

class PrintTests(TestCase):
    """
    Tests for Prints model
    """

    def test_str(self):
        print_title = 'Mona Lisa'
        self.assertEqual(str(print_title),'Mona Lisa')
