from collections import deque


class ContextManager:

    def __init__(self, max_history=20):

        self.history = deque(maxlen=max_history)

    # -------------------------

    def add_user(self, message):

        self.history.append({

            "role": "user",

            "text": message

        })

    # -------------------------

    def add_ai(self, message):

        self.history.append({

            "role": "assistant",

            "text": message

        })

    # -------------------------

    def get_history(self):

        return list(self.history)

    # -------------------------

    def clear(self):

        self.history.clear()

    # -------------------------

    def last_message(self):

        if len(self.history) == 0:

            return None

        return self.history[-1]

    # -------------------------

    def print_history(self):

        print("\n========== Conversation ==========\n")

        for item in self.history:

            print(f"{item['role'].upper()} : {item['text']}")

        print("\n==================================\n")


context = ContextManager()