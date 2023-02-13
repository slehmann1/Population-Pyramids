from django.test import TestCase
from geotree.scripts import geo_load


class GeoLoadTests(TestCase):
    def test_gen_col_name(self):
        self.assertEqual(geo_load.gen_col_name(2020, 2, True), "m_20_2")
        self.assertEqual(geo_load.gen_col_name(2001, 0, False), "f_01_0")
        self.assertEqual(geo_load.gen_col_name(2018, 30, True), "m_18_30")

    def test_pascal_case_space(self):
        self.assertEqual(geo_load.pascal_case_space("hello world"), "Hello World")
        self.assertEqual(geo_load.pascal_case_space("hELlo World"), "Hello World")
        self.assertEqual(geo_load.pascal_case_space("Hello"), "Hello")
        self.assertEqual(geo_load.pascal_case_space("HELLO world"), "Hello World")
        