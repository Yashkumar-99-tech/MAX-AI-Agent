from core.startup import startup
from core.command_router import router
from voice.listen import listen
from voice.speak import speak

print("=" * 60)

startup.banner()
startup.loading()

speak("Hello Yash. MAX AI is now online.")

while True:

    user = listen().strip()

    if not user:
        continue

    if user.lower() in ["exit", "quit", "goodbye", "stop"]:

        speak("Goodbye Yash. Have a nice day.")

        break

    reply = router.execute(user)


    print("\n🤖 MAX :", reply)

    speak(reply)
    import time

time.sleep(0.5)
