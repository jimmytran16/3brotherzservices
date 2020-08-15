import unittest
from main import app


class TestConstructionContent(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.test = True

    def tearDown(self):
        pass


    def test_check_home_page(self):
        response = self.app.get('/home/')
    def test_check_home_page(self):
        response = self.app.get('/home/')
    def test_check_home_page(self):
        response = self.app.get('/home/')
    def test_check_home_page(self):
        response = self.app.get('/home/')
    def test_check_home_page(self):
        response = self.app.get('/home/')
    def test_check_home_page(self):
        response = self.app.get('/home/')
    def test_check_home_page(self):
        response = self.app.get('/home/')
    def test_check_home_page(self):
        response = self.app.get('/home/')
    def test_check_home_page(self):
        response = self.app.get('/home/')
    def test_check_home_page(self):
        response = self.app.get('/home/')
