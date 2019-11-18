# Get the random functionality provided by Python
import random

print("Hello and welcome to Code Adventure!")

# whether the player is alive
alive = True

# whether we are processing an action
doing_action = False

player = {
    "health": random.randint(10, 40),
    "weapons": [
        {
            "name": "Dagger",
            "attack": random.randint(10, 20),
        },
    ],
}

enemies = []

max_enemies = 2

# While the player is alive
while alive:

    # Prompt the player for an action
    action = input("Enter a number: 1 - Attack, 2 - Item, 3 - Exit > ")

    # If the player wants to attack
    if action == "1":

        for _ in range(random.randint(1, max_enemies + 1)):
            enemy = {
                "name": random.choice(["Goomba", "Koopa", "Paratroopa"]),
                "health": random.randint(10, 100),
                "attack": random.randint(1, 10),
            }
            enemies.append(enemy)

            # Print out something special if the enemy has max health
            if enemy["health"] == 100:
                print("Deathwing is coming...")   

        # Start the battle
        doing_action = True
        while doing_action:
            weapon = player["weapons"][0]
            enemy = enemies[0]

            input("Press enter to attack the first enemy!\n")

            enemy["health"] -= weapon["attack"]

            print(f"You attacked the {enemy['name']}! Lost {weapon['attack']} health, {enemy['health']} remaining.")

            # if the enemy has died
            if enemy["health"] <= 0:
                print(f"You killed the {enemy['name']}!")
                
                del enemies[0]

                if enemies == []:
                    print("You won the battle!")
                    # leave just the action, not the main loop
                    doing_action = False
                    continue

            for enemy in enemies:
                player["health"] -= enemy["attack"]

                print(f"A {enemy['name']} attacks! Lost {enemy['attack']} health, {player['health']} remaining.")

                # If the player has died
                if player["health"] <= 0:
                    print("You died...")
                    # leave the action
                    doing_action = False
                    # set alive to False so we exit the main loop
                    alive = False

    elif action == "2":
        # TODO impl item logic
        # NOTE we will implement this function on the 18th!
        pass

    elif action == "3":
        # say goodbye and exit the main loop
        print("Goodbye!")
        alive = False

    else:
        # if action is not 1, 2, or 3, ask for another action
        print("Not a valid choice!")
