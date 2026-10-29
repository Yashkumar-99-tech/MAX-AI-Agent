from core.startup import startup
from core.command_router import router
from memory.context_manager import context
from voice.speak import speak
from voice.listen import listen
import os

print("Current Folder :", os.getcwd())

print("=" * 60)

startup.banner()

startup.loading()

speak("Hello Yash. MAX AI is ready.")

while True:

    # 🎤 Listen from microphone
    user = listen().strip()

    # If nothing recognized, listen again
    if not user:
        continue

    # Exit command
    if user.lower() in [
        "exit",
        "quit",
        "goodbye",
        "stop max",
        "bye"
    ]:

        context.print_history()

        print("\n👋 Goodbye Yash!")

        speak("Goodbye Yash. Have a nice day.")

        break

    try:

        print(f"\n🧑 You : {user}")

        reply = router.execute(user)

        if not reply:
            reply = "Sorry Yash, I could not understand."

        reply = str(reply)

        print(f"\n🤖 MAX : {reply}")

        speak(reply)

    except Exception as e:

        print("Error :", e)

        speak("Sorry Yash, something went wrong.")