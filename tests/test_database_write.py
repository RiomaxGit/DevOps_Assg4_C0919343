import unittest
from pymongo import MongoClient

class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        """Set up the connection to MongoDB and target the products collection."""
        self.client = MongoClient("MDB_URI")  # Removed actual string.
        self.db = self.client.shop_db
        self.collection = self.db.products

    def test_insert_document(self):
        """Test inserting a document into MongoDB and verifying it."""
        test_document = {
            "name": "Smartphone",
            "tag": "Electronics",
            "price": 699.99,
            "image_path": "static/images/smartphone.jpg"
        }
        result = self.collection.insert_one(test_document)
        self.assertIsNotNone(result.inserted_id)
        found_document = self.collection.find_one({"_id": result.inserted_id})
        self.assertIsNotNone(found_document)
        self.assertEqual(found_document['name'], "Smartphone")
        self.assertEqual(found_document['tag'], "Electronics")
        self.assertEqual(found_document['price'], 699.99)
        self.assertEqual(found_document['image_path'], "static/images/smartphone.jpg")

    def test_find_existing_document(self):
        """Test finding an existing document in MongoDB."""
        query = {"name": "Laptop"}
        found_document = self.collection.find_one(query)
        self.assertIsNotNone(found_document)
        self.assertEqual(found_document['name'], "Laptop")
        self.assertEqual(found_document['tag'], "Electronics")
        self.assertEqual(found_document['price'], 899.99)
        self.assertEqual(found_document['image_path'], "static/images/laptop.jpg")

    def test_find_nonexistent_document(self):
        """Test that a nonexistent document is not found."""
        query = {"name": "dummy"}
        found_document = self.collection.find_one(query)
        self.assertIsNone(found_document)

if __name__ == "__main__":
    unittest.main()
