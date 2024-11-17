from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI

class StockChatbot:
    def __init__(self):
        self.memory = ConversationBufferMemory()
        self.chat_model = ChatOpenAI(model="gpt-3.5-turbo")
        
        self.chain = ConversationChain(
            llm=self.chat_model,
            memory=self.memory,
        )

    def ask(self, question: str):
        return self.chain.run(question)

if __name__ == "__main__":
    bot = StockChatbot()
    print("Chatbot is running. Type your questions.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = bot.ask(user_input)
        print(f"Bot: {response}")
