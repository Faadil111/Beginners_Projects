command = ""
Start = False
while True:
    command = input("> ").lower()
    if command == "start":
        if Start:
            print("Car has already started")
        else:
            Start = True
            print("Car has started moving......")
    elif command == "stop":
        if not Start:
            print("Car has already been stopped")
        else:
            Start = False
            print("Car has stopped....")
    elif command == "help":
        print( """
start - Start car
stop - Stop car
quit - Quit game
""")
    elif command == "quit":
        break
    else:
        print("I don't know what you're saying")