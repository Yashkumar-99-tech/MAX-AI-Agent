from ai.api_manager import APIManager

brain = APIManager()

def ask_ai(question):
    return brain.send(question)