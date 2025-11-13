import unittest
from src.client_queue import insert_client, buys

class TestClientQueue(unittest.TestCase):

    def test_insert_client_adds_client(self):
        queue = {}
        insert_client(queue, 1, 50)
        self.assertIn(1, queue)
        self.assertEqual(queue[1], 50)

    def test_buys_successful_purchase(self):
        queue = {1: 100}
        success, remaining = buys(queue, 1, 40)
        self.assertTrue(success)
        self.assertEqual(remaining, 60)

    def test_buys_insufficient_funds(self):
        queue = {1: 30}
        success, remaining = buys(queue, 1, 50)
        self.assertFalse(success)
        self.assertEqual(remaining, 30)

    def test_multiple_purchases(self):
        queue = {1: 100}
        buys(queue, 1, 30)
        success, remaining = buys(queue, 1, 50)
        self.assertTrue(success)
        self.assertEqual(remaining, 20)

    def test_insert_client_existing_id(self):
        queue = {1: 20}
        success_first = insert_client(queue, 2, 80)
        self.assertTrue(success_first)
        success_second = insert_client(queue, 2, 30)
        self.assertFalse(success_second)

if __name__ == '__main__':
    unittest.main()