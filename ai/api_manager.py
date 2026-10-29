import time

from google import genai
from google.genai import types

from config import API_KEYS, MODEL_NAME
from ai.prompt import SYSTEM_PROMPT


class APIManager:

    def __init__(self):

        self.current_index = 0
        self.client = None
        self.chat = None

        self.connect()

    def connect(self):

        api_key = API_KEYS[self.current_index]

        self.client = genai.Client(
            api_key=api_key
        )

        self.chat = self.client.chats.create(
            model=MODEL_NAME,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

        print(f"✅ Connected using API {self.current_index + 1}")

    def switch_api(self):

        self.current_index = (self.current_index + 1) % len(API_KEYS)

        print("🔄 Switching API...")

        self.connect()

    def send(self, message):

        retries = 3

        while retries > 0:

            try:

                response = self.chat.send_message(message)

                return response.text

            except Exception as e:

                error = str(e)

                print("\nAPI Error :", error)

                # High Demand
                if "503" in error or "UNAVAILABLE" in error:

                    print("⏳ Gemini Server Busy... Retrying in 5 seconds...")

                    time.sleep(5)

                    retries -= 1

                    continue

                # Rate Limit
                if "429" in error:

                    print("⏳ Rate Limit... Waiting 10 seconds...")

                    time.sleep(10)

                    retries -= 1

                    continue

                # Unauthorized
                if "401" in error:

                    print("❌ Invalid API Key")

                    self.switch_api()

                    retries -= 1

                    continue

                # Other Errors
                print("⚠ Unknown Error")

                self.switch_api()

                retries -= 1

        return "❌ MAX AI couldn't connect to Gemini right now. Please try again after a few moments."