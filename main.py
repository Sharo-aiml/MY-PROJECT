from agents.coordinator import Coordinator
from utils.speech import speak, listen
from tools.reminder_tool import init_db

def main():

    init_db()

    coordinator = Coordinator()

    print("AI Assistant Ready")

    while True:

        choice = input("1.Text 2.Voice 3.Exit: ")

        if choice == "1":

            text = input("You: ")

        elif choice == "2":

            text = listen()

        else:
            break

        response = coordinator.handle(text)

        print("Assistant:", response)

        speak(str(response))


if __name__ == "__main__":
    main()