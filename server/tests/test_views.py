from django.test import TestCase
from geotree import views

class ViewsTests(TestCase):
    def test_round_max(self):
        self.assertEqual(views.DetailView.round_max(1025), 1100)
        self.assertEqual(views.DetailView.round_max(23335), 24000)
        self.assertEqual(views.DetailView.round_max(33335), 40000)
        self.assertEqual(views.DetailView.round_max(92), 100)