import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():

    with sr.Microphone() as source:

        print("\n🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        except sr.WaitTimeoutError:

            return ""

    try:

        text = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print(f"\n🧑 You : {text}")

        return text.lower()

    except sr.UnknownValueError:

        return ""

    except sr.RequestError:

        print("Internet Error")

        return ""