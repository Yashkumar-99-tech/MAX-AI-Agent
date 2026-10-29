from google import genai



response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Reply with only one word: Hello"
)

print(response.text)