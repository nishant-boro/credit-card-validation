import unittest
import app
import json

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()
        self.headers = {'Content-Type': 'application/json'}

    def test_validation(self):
        self.headers['no'] = '370000000000002'
        self.headers['month'] = '02'
        self.headers['year'] = '2030'
        self.headers['cvc'] = '7373'
        response = self.app.get("/validate", headers=self.headers)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['valid'], 'true')
        if json_response['valid'] == True:
            print("The brand of the card is: " + json_response['brand'])