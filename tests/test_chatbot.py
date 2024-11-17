import unittest
from chatbot.chatbot import StockChatbot

class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.bot = StockChatbot()

    def test_response(self):
        response = self.bot.ask("Hello, what is your purpose?")
        self.assertIsNotNone(response)

if __name__ == "__main__":
    unittest.main()