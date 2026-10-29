from core.intent_engine import intent_engine

tests = [

    "play kesariya",

    "open youtube",

    "remember my birthday",

    "take screenshot",

    "what is quantum computing"

]

for command in tests:

    print(command)

    print(intent_engine.detect(command))

    print("-" * 40)