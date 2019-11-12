# Get the random functionality provided by Python
import random

print("Hello and welcome to Code Adventure!")

# whether the player is alive
alive = True

# whether we are processing an action
doing_action = False

player_health = 10
player_attack = 15

# While the player is alive
while alive:

    # Prompt the player for an action
    action = input("Enter a number: 1 - Attack, 2 - Item, 3 - Exit")

    # If the player wants to attack
    if action == "1":

        # enemy health = random value from 10 to 100
        enemy_health = random.randint(10, 100)

        # Print out something special if the enemy has max health
        if enemy_health == 100:
            print("Deathwing is coming...")

        # Start the battle
        doing_action = True
        while doing_action:

            # Calculate enemy attack (from 0 to 5)
            enemy_attack = random.randint(0, 5)

            # Lose health
            player_health = player_health - enemy_attack

            print("A Goomba attacks! Lost X health, Y remaining.")

            # If the player has died
            if player_health <= 0:
                print("You died...")
                # leave the action
                doing_action = False
                # set alive to False so we exit the main loop
                alive = False

            else:
                input("Press enter to attack!")
                # Make the enemy lose health
                enemy_health = enemy_health - player_attack

                print("You attacked the Goomba! Lost X health, Y remaining.")

                # if the enemy has died
                if enemy_health <= 0:
                    print("You won the battle!")
                    # leave just the action, not the main loop
                    doing_action = False

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
