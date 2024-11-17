import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_invalid_method(self):
        """Test that POST request to /products returns 405 status code."""
        response = self.app.post('/products')  # Invalid method
        self.assertEqual(response.status_code, 405)

if __name__ == "__main__":
    unittest.main()
