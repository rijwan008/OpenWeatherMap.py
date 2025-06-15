import nltk
from nltk.chat.util import Chat, reflections

# List of conversation patterns and responses
pairs = [
    [r"my name is (.*)", ["Hello %1, how can I assist you today?"]],
    [r"(hi|hello|hey)", ["Hi there!", "Hello! How can I help you?"]],
    [r"what is your name?", ["I'm a Python chatbot created with NLTK."]],
    [r"how are you ?", ["I'm good, thank you!"]],
    [r"sorry (.*)", ["It's okay. No worries."]],
    [r"(.*) (location|city)", ["I'm a virtual assistant, I exist in your imagination!"]],
    [r"(.*) help (.*)", ["Sure, I can help. Please tell me your question."]],
    [r"(.*) (created|made) you?", ["I was created by a Python developer using NLTK."]],
    [r"quit", ["Goodbye! Have a nice day."]],
    [r"(.*)", ["I'm not sure I understand. Could you rephrase that?"]]
]

# Create and start the chatbot
def start_chat():
    print("Hi! I am your chatbot. Type 'quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
if __name__ == "__main__":
    start_chat()
