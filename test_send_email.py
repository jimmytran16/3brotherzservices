import unittest
from app import app

class TestEmailSends(unittest.TestCase): #test email sending functionality // Make sure all contact/quote forms are being sent successfully

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        print('passed')

    def send_quote_form(self,firstname,lastname,email,phone,message,location):
        return self.app.post(
            '/submit-quote/',
            data=dict(first_name=firstname,last_name=lastname,email=email,phone=phone,message=message,city_state=location),
            follow_redirects=True
        )

    def send_contact_form(self,firstname,lastname,email,phone,message):
        return self.app.post(
            '/submit-contact-form/',
            data=dict(first_name=firstname,last_name=lastname,email=email,phone=phone,message=message),
            follow_redirects=True
        )

    def test_contact_quote_submission(self): #test submission form for contact
        response = self.send_quote_form('jimmy','tran','jimmytran1620@gmail.com','781-267-1202','contact test','boston,ma')
        self.assertEqual(response.status_code,200)

    def test_quote_contact_submission(self): #test submission form for contact
        response = self.send_contact_form('jimmy','tran','jimmytran1620@gmail.com','781-267-1202','quote test')
        self.assertEqual(response.status_code,200)

if __name__=='__main__':
    unittest.main()
