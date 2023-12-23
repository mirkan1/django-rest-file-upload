from django.test import TestCase
from quickstart.models import File
from django.utils import timezone

# models test
class UploadTest(TestCase):

    def create_file(self, name="only a test.txt", data="yes, this is only a test"):
        return File.objects.create(name=name, data=data, created_at=timezone.now())

    def test_whatever_creation(self):
        w = self.create_file()
        self.assertTrue(isinstance(w, File))
        self.assertEqual(w.__unicode__(), w.name)
