import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_index_returns_200(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_hello_returns_json(self):
        res = self.client.get("/hello")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.get_json(), {"message": "Hello!"})

if __name__ == "__main__":
    unittest.main()
