import unittest
from ..app.main import app


class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_getdata_codes(self):
        response = self.app.get('/codes')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"AL", response.data)  # Assuming 'AL' is part of your codes data

    def test_getdata_states(self):
        response = self.app.get('/states')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alabama", response.data)  # Assuming 'alabama' is part of your states data

    def test_getdata_invalid_option(self):
        response = self.app.get('/invalid')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Error: Invalid option", response.data)

    def test_welcome(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to dataservice", response.data)

if __name__ == '__main__':
    unittest.main()
