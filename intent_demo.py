from brain.intents import IntentDetector

def main():
    detector = IntentDetector()
    while True:
        text = input("You : ")
        print(detector.detect(text))

if __name__ == '__main__':
    main()
