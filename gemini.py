import random
import matplotlib.pyplot as plt
import argparse


def monty_hall_simulation(num_trials, switch_doors, num_doors=3):
    """
    Simulates the Monty Hall problem for a specified number of trials and doors.

    Args:
        num_trials (int): The number of times to run the simulation.
        switch_doors (bool): Whether the player switches doors after Monty's reveal.
        num_doors (int): The total number of doors in the game.

    Returns:
        float: The win rate (number of wins / total trials).
    """
    wins = 0
    for _ in range(num_trials):
        car_door = random.randint(0, num_doors - 1)
        player_choice = random.randint(0, num_doors - 1)

        # Monty reveals goat doors (all but two: player choice and car door)
        possible_reveals = [i for i in range(num_doors) if i != car_door and i != player_choice]

        # Randomly choose doors for Monty to reveal until only 2 are left.
        while len(possible_reveals) > (num_doors - 2):
            reveal_choice = random.choice(possible_reveals)
            possible_reveals.remove(reveal_choice)

        monty_reveal = possible_reveals[0]  # could be more than one door

        if switch_doors:
            player_choice = [i for i in range(num_doors) if i != player_choice and i not in possible_reveals][0]

        if player_choice == car_door:
            wins += 1

    return wins / num_trials


def run_simulation(num_doors, num_trials=10000):
    """Runs the simulation and displays results."""

    switch_win_rate = monty_hall_simulation(num_trials, True, num_doors)
    stay_win_rate = monty_hall_simulation(num_trials, False, num_doors)

    print(f"Number of doors: {num_doors}")
    print(f"Win rate when switching doors: {switch_win_rate:.4f}")
    print(f"Win rate when staying with the original choice: {stay_win_rate:.4f}")

    labels = ['Switch Doors', 'Stay with Original Choice']
    win_rates = [switch_win_rate, stay_win_rate]

    plt.bar(labels, win_rates, color=['blue', 'red'])
    plt.ylabel('Win Rate')
    plt.title(f'Monty Hall Simulation Results ({num_doors} Doors)')
    plt.ylim(0, 1)
    plt.show()

def interactive_menu():
    """Displays the interactive console menu."""
    while True:
        print("\nMonty Hall Simulation Menu:")
        print("1. Run the problem with 3 doors")
        print("2. Run the problem with 10 doors")
        print("3. Run the problem with 1000 doors")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            run_simulation(3)
        elif choice == '2':
            run_simulation(10)
        elif choice == '3':
            run_simulation(1000)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


def main():
    parser = argparse.ArgumentParser(description="Monty Hall Problem Simulation")
    parser.add_argument("-i", "--interactive", action="store_true", help="Run in interactive mode")
    args = parser.parse_args()

    if args.interactive:
        interactive_menu()
    else:
       #default behaviour, 3 doors
        run_simulation(3)



if __name__ == "__main__":
    main()