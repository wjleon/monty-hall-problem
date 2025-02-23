"""
Monty Hall Simulation Script

Author: Wilmer Leon (modified by ChatGPT)
Contact: https://www.linkedin.com/in/wilmer-leon/
Note: This file was 100% generated with ChatGPT (o3 mini high).

Description:
This script simulates the Monty Hall problem, a classic probability puzzle.
It demonstrates the win rates for both switching doors and staying with the
original choice. You can run the simulation for a configurable number of doors.
The script supports an interactive mode (via the -i or --interactive argument)
to choose among:
    1. 3 doors
    2. 10 doors
    3. 1000 doors

Usage:
    # Run default simulation (3 doors):
    python monty_hall_simulation.py

    # Run in interactive mode:
    python monty_hall_simulation.py -i

Dependencies:
- Python 3.6 or higher
- `random` package (built-in)
- `matplotlib` package (install with `pip install matplotlib`)
- `argparse` package (built-in)
"""

import random
import matplotlib.pyplot as plt
import argparse

def monty_hall_simulation(num_trials, num_doors, switch_doors):
    """
    Simulates the Monty Hall problem for a specified number of trials and doors.
    In the extended version, Monty opens all doors except two: the player's initial 
    choice and one other door. The remaining door is:
      - The car door, if the player's initial pick was wrong.
      - A random goat door, if the player's initial pick was the car.
      
    Args:
        num_trials (int): Number of simulation runs.
        num_doors (int): Number of doors in the simulation.
        switch_doors (bool): If True, the player switches to the remaining door.
        
    Returns:
        float: The win rate (wins / num_trials).
    """
    wins = 0  # Counter for wins

    for _ in range(num_trials):
        # Randomly assign the car behind one of the doors (0 to num_doors-1)
        car_door = random.randint(0, num_doors - 1)

        # Player makes an initial random choice
        player_choice = random.randint(0, num_doors - 1)

        if switch_doors:
            # In the extended Monty Hall, Monty opens all doors except two:
            # the player's door and one other door.
            if player_choice == car_door:
                # If the player's initial pick is correct, Monty randomly leaves one goat door closed.
                remaining_doors = [i for i in range(num_doors) if i != player_choice]
                final_choice = random.choice(remaining_doors)
            else:
                # If the player's initial pick is wrong, Monty leaves the car door closed.
                final_choice = car_door
        else:
            # If not switching, the player's final choice remains the initial pick.
            final_choice = player_choice

        if final_choice == car_door:
            wins += 1

    return wins / num_trials

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Monty Hall Simulation Script")
    parser.add_argument('-i', '--interactive', action='store_true',
                        help="Run in interactive mode with a console menu.")
    args = parser.parse_args()

    # Determine the number of doors based on interactive mode or default
    if args.interactive:
        print("Monty Hall Simulation Interactive Menu")
        print("1: Run the problem with 3 doors")
        print("2: Run the problem with 10 doors")
        print("3: Run the problem with 1000 doors")
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == "1":
            num_doors = 3
        elif choice == "2":
            num_doors = 10
        elif choice == "3":
            num_doors = 1000
        else:
            print("Invalid choice. Defaulting to 3 doors.")
            num_doors = 3
    else:
        # Default simulation uses 3 doors.
        num_doors = 3

    num_trials = 10000  # Number of trials for the simulation

    # Run the simulation for both strategies
    switch_win_rate = monty_hall_simulation(num_trials, num_doors, True)
    stay_win_rate = monty_hall_simulation(num_trials, num_doors, False)

    # Print the results
    print(f"\nSimulation with {num_doors} doors and {num_trials} trials:")
    print(f"Win rate when switching doors: {switch_win_rate:.4f}")
    print(f"Win rate when staying with the original choice: {stay_win_rate:.4f}")

    # Generate the bar chart
    labels = ['Switch Doors', 'Stay with Original Choice']
    win_rates = [switch_win_rate, stay_win_rate]
    plt.bar(labels, win_rates, color=['blue', 'red'])
    plt.ylabel('Win Rate')
    plt.title(f'Monty Hall Simulation Results\n(Chatgpt o3 mini high)  ({num_doors} doors)')
    plt.ylim(0, 1)
    plt.show()

if __name__ == "__main__":
    main()
