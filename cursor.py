"""
Monty Hall Simulation Script

Author: Wilmer Leon
Contact: https://www.linkedin.com/in/wilmer-leon/
Note: This file was 100% generated with Cursor (Claude 3.5 Sonnet).

Description:
This script simulates the Monty Hall problem, a classic probability puzzle.
It demonstrates the win rates for both switching doors and staying with the
original choice. The script supports a configurable number of trials and
visualizes the results using matplotlib.

Usage:
Run the script with the following command:
    python monty_hall_simulation.py          # Run with default 3 doors
    python monty_hall_simulation.py -i       # Run in interactive mode
    python monty_hall_simulation.py --interactive  # Run in interactive mode

Dependencies:
- Python 3.6 or higher
- `random` package (built-in)
- `matplotlib` package (install with `pip install matplotlib`)
- `argparse` package (built-in)
"""

import random
import matplotlib.pyplot as plt
import argparse

def monty_hall_simulation(num_trials, switch_doors, num_doors=3):
    """
    Simulates the Monty Hall problem for a specified number of trials and doors.

    Args:
        num_trials (int): The number of times to run the simulation.
        switch_doors (bool): Whether the player switches doors after Monty's reveal.
        num_doors (int): The number of doors in the game (default: 3)

    Returns:
        float: The win rate (number of wins / total trials).
    """
    wins = 0
    for _ in range(num_trials):
        # Randomly assign the car to one of the doors
        car_door = random.randint(0, num_doors - 1)
        
        # Player makes a random initial choice
        player_choice = random.randint(0, num_doors - 1)
        
        # Monty reveals all but one door that doesn't have the car and isn't the player's choice
        available_doors = set(range(num_doors))
        available_doors.remove(player_choice)
        if car_door != player_choice:
            available_doors.remove(car_door)
            
        # Remove all but one door (Monty reveals all others)
        while len(available_doors) > 1:
            available_doors.remove(random.choice(list(available_doors)))

        if switch_doors:
            # Switch to the remaining door
            player_choice = available_doors.pop() if car_door == player_choice else car_door

        if player_choice == car_door:
            wins += 1

    return wins / num_trials

def run_simulation(num_doors):
    """
    Runs the simulation for a specific number of doors and displays results.
    
    Args:
        num_doors (int): The number of doors to use in the simulation
    """
    num_trials = 10000
    switch_win_rate = monty_hall_simulation(num_trials, True, num_doors)
    stay_win_rate = monty_hall_simulation(num_trials, False, num_doors)

    print(f"\nResults for {num_doors} doors:")
    print(f"Win rate when switching doors: {switch_win_rate:.4f}")
    print(f"Win rate when staying with the original choice: {stay_win_rate:.4f}")

    # Visualize the results using a bar chart
    labels = ['Switch Doors', 'Stay with Original Choice']
    win_rates = [switch_win_rate, stay_win_rate]

    plt.figure()
    plt.bar(labels, win_rates, color=['blue', 'red'])
    plt.ylabel('Win Rate')
    plt.title(f'Monty Hall Simulation Results ({num_doors} doors)')
    plt.ylim(0, 1)
    plt.show()

def display_menu():
    """Displays the interactive menu and handles user input."""
    while True:
        print("\nMonty Hall Simulation Menu:")
        print("1. Run simulation with 3 doors")
        print("2. Run simulation with 10 doors")
        print("3. Run simulation with 1000 doors")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            run_simulation(3)
        elif choice == '2':
            run_simulation(10)
        elif choice == '3':
            run_simulation(1000)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Monty Hall Problem Simulation')
    parser.add_argument('-i', '--interactive', action='store_true',
                        help='Run in interactive mode with menu')
    
    args = parser.parse_args()
    
    if args.interactive:
        display_menu()
    else:
        # Run default simulation with 3 doors
        run_simulation(3)

if __name__ == "__main__":
    main()