# coding:utf-8

from django.test import TestCase
from .models import AreaStatus
# Create your tests here.
from django.utils import timezone

class AreaStatusTestCase(TestCase):
    def setUp(self):
        AreaStatus.objects.create(state='123')

        

    def test_Area_str(self):
        A1 = AreaStatus.objects.get(state='123')
        # elf.assertEqual(str(A1),"正在检修")
        self.assertEqual(A1.state,'1233')

