import unittest
from main import app

# Check if webpage content matches the routings
class TestConstructionContent(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.test = True

    def tearDown(self):
        pass

    def test_check_home_page(self):
        response = self.app.get('/home/')
        self.assertIn(b'Dedicated to offering the highest quality services in carpentry, flooring, and painting.',response.data)

    def test_check_quote_page(self):
        response = self.app.get('/get-your-quote/')
        self.assertIn(b'Request for Quote',response.data)

    def test_check_services_page(self):
        response = self.app.get('/services/')
        self.assertIn(b'<h3 class="mt-0 text-black">Remodeling</h3>',response.data)

    def test_check_contact_page(self):
        response = self.app.get('/contact/')
        self.assertIn(b'Leave a message or question',response.data)

    def test_check_about_us_page(self):
        response = self.app.get('/aboutus/')
        self.assertIn(b'Company History',response.data)

    def test_check_more_work_page(self):
        response = self.app.get('/more-work/')
        self.assertIn(b'<title> Works </title>',response.data)

    def test_check_our_work_page(self):
        response = self.app.get('/our-works/')
        self.assertIn(b'<h1>Our recent works</h1>',response.data)

    def test_submit_quote_not_allowed(self):
        response = self.app.get('/submit-quote/')
        self.assertIn(b'<h1>Method Not Allowed</h1>', response.data)

    def test_submit_contact_not_allowed(self):
        response = self.app.get('/submit-quote/')
        self.assertIn(b'<p>The method is not allowed for the requested URL.</p>', response.data)



if __name__ == '__main__':
    unittest.main()
