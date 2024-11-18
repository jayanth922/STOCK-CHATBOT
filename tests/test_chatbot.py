import unittest
from chatbot import StockChatbot


class TestStockChatbot(unittest.TestCase):
    def setUp(self):
        """Set up the chatbot instance for testing."""
        self.bot = StockChatbot()

    def test_ask_question(self):
        """Test that the chatbot returns a response to a user question."""
        question = "What is the stock price of Tesla?"
        response = self.bot.ask(question)
        self.assertIsInstance(response, str)  # Ensure the response is a string
        self.assertTrue(len(response) > 0)   # Ensure the response is not empty


if __name__ == "__main__":
    unittest.main()
