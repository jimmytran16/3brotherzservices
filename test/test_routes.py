from app import app
import unittest

class RouteTests(unittest.TestCase): # test ran for routes // Make sure all requests have successful response

    def setUp(self):
        self.app = app.test_client() #init a client instance

    def tearDown(self):
        print('PASSED')

    def test_main_page(self):
        response = self.app.get('/',follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_main_page_2(self):
        response = self.app.get('/home/',follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_get_your_quote_page(self):
        response = self.app.get('/get-your-quote/',follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_services_page(self):
        response = self.app.get('/services/',follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_contact_page(self):
        response = self.app.get('/contact/',follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_about_us_page(self):
        response = self.app.get('/aboutus/',follow_redirects=True)
        self.assertEqual(response.status_code,200)

    def test_our_works_page(self):
        response = self.app.get('/our-works/',follow_redirects=True)
        self.assertEqual(response.status_code,200)


if __name__ == '__main__':
    unittest.main()
