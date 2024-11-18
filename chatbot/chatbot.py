from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

import os
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

class StockChatbot:
    def __init__(self):
        self.memory = ConversationBufferMemory()
        self.chat_model = ChatGroq(  
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="mixtral-8x7b-32768",
        )
        self.chain = ConversationChain(
            llm=self.chat_model,
            memory=self.memory,
        )

    def ask(self, question: str):
        return self.chain.run(question)

if __name__ == "__main__":
    bot = StockChatbot()
    print("Chatbot is running. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = bot.ask(user_input)
        print(f"Bot: {response}")
