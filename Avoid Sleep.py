# Start the game
def start():
    print("Welcome to *Avoid Sleep*")
    print("You need your environment to be clean without falling asleep as you would need to study soon")
    print("Do you: ")
    print("1. Go to the main floor")
    print("2. Do you stay in the basement")

    choice = get_choice(["1", "2"])
# Depending on what choice you make, a function will be called
    if choice == "1":
        main_floor()

    else:
        basement()

def main_floor():
    print("\nYou go to the main floor. You have to either:")
    print("1. Go to the sitting room")
    print("2. Go to the dining room")

    choice = get_choice(["1", "2"])
    if choice == "1":
        siting_room()

    else:
        dining_room()


def basement():
    print("\nYou stay in the basement. You have to either:")
    print("1. Stay in your room")
    print("2. Go to the bathroom")

    choice = get_choice(["1", "2"])
    if choice == 1:
        room()
    else:
        bathroom()

def siting_room():
    print("\nYou came to the sitting room. You have to either:")
    print("1. Sweep the floor")
    print("2. Arrange the couch")

    choice = get_choice(["1", "2"])
    if choice == 1:
        print("\nNice ! You picked the right choice, after sweeping you'll be energized enough to read. YOU WON")
    else:
        print("You picked the wrong choice, after arranging the couch you'll be deceived by your other self to sleep. GAME OVER")

def dining_room():
    print("\nYou came to the dining room. You have to either:")
    print("1. Clean the floor")
    print("2. Clean the chair")

    choice = get_choice(["1", "2"])
    if choice == 1:
        print("You picked the right choice, after cleaning the floor you'll be energized enough to read. YOU WON")
    else:
        print("You picked the wrong choice, after cleaning the chair you'll be deceived by your other self to sleep. GAME OVER")

def room():
    print("\nYou stayed in your room. You have to either:")
    print("1. Clean the floor")
    print("2. Lay your bed")

    choice = get_choice(["1", "2"])
    if choice == 1:
        print("You picked the right choice, after cleaning the floor you'll be energized enough to read. YOU WON")
    else:
        print("You picked the wrong choice, after laying your bed you'll be deceived by your other self to sleep. GAME OVER")

def bathroom():
    print("\nYou went to the bathroom. You have to either:")
    print("1. Mop the floor")
    print("2. Take a nice hot shower")

    choice = get_choice(["1", "2"])
    if choice == 1:
        print("You picked the right choice, after mopping the floor you'll be energized enough to read. YOU WON")
    else:
        print("You picked the wrong choice, after taking a nice hot shower you'll be deceived by your other self to sleep. GAME OVER")


# This function helps to check the choice you made
def get_choice(valid_choices):
    while True:
        choice = input("Enter your choice: ").strip()
        if choice in valid_choices:
            return choice
        elif choice == "q":
            print("Thank you for playing")
            break
        else:
            print("Invalid input. Please choose one of the options:", ', '.join(valid_choices))


start()