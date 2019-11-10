print("Hello and welcome to Code Adventure!")

alive = True

while alive:
    action = input("Enter a number: 1 - Fight, 2 - Item, 3 - Exit")

    if action == "1":
        # TODO impl fight logic
        pass

    elif action == "2":
        # TODO impl item logic
        pass

    elif action == 3:
        print("Goodbye!")
        alive = False

    else:
        print("Not a valid choice!")