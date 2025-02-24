"""
Monty Hall Simulation Script

Author: Wilmer Leon
Contact: https://www.linkedin.com/in/wilmer-leon/
Note: This file was 100% generated with ChatGPT (4o model).

Description:
This script simulates the Monty Hall problem, a classic probability puzzle.
It demonstrates the win rates for both switching doors and staying with the
original choice. The script supports a configurable number of trials and
visualizes the results using matplotlib.

Usage:
Run the script with the following command:
    python monty_hall_simulation.py -i

Dependencies:
- Python 3.6 or higher
- `random` package (built-in)
- `matplotlib` package (install with `pip install matplotlib`)
"""

import random
import matplotlib.pyplot as plt
import argparse
import os

def monty_hall_simulation(num_trials, switch_doors, num_doors):
    """
    Simulates the Monty Hall problem for a specified number of trials and doors.

    Args:
        num_trials (int): The number of times to run the simulation.
        switch_doors (bool): Whether the player switches doors after Monty's reveal.
        num_doors (int): The number of doors in the simulation.

    Returns:
        float: The win rate (number of wins / total trials).
    """
    wins = 0  # Initialize the win counter
    for _ in range(num_trials):  # Iterate through each trial
        # Randomly assign the car to one of the doors
        car_door = random.randint(0, num_doors - 1)

        # Player makes a random initial choice of doors
        player_choice = random.randint(0, num_doors - 1)

        # Monty reveals a goat behind a door that is NOT the car and NOT the player's choice.
        monty_reveal = random.choice([i for i in range(num_doors) if i != car_door and i != player_choice])

        # If the player switches doors:
        if switch_doors:
            # Determine the door to switch to.
            # It must be different from the player's original choice and Monty's reveal.
            player_choice = [i for i in range(num_doors) if i != player_choice and i != monty_reveal][0]

        # Check if the player's final choice (after potentially switching) is the car door.
        if player_choice == car_door:
            wins += 1  # Increment the win counter if the player won.

    return wins / num_trials  # Calculate and return the win rate.

def run_simulation(num_doors):
    """
    Runs the Monty Hall simulation for a specified number of doors and displays the results.

    Args:
        num_doors (int): The number of doors in the simulation.
    """
    num_trials = 10000  # Set the number of trials for the simulations
    switch_win_rate = monty_hall_simulation(num_trials, True, num_doors)  # Simulate with switching doors
    stay_win_rate = monty_hall_simulation(num_trials, False, num_doors)  # Simulate without switching doors

    # Print the results to the console
    print(f"Win rate when switching doors: {switch_win_rate:.4f}")
    print(f"Win rate when staying with the original choice: {stay_win_rate:.4f}")

    # Visualize the results using a bar chart
    labels = ['Switch Doors', 'Stay with Original Choice']  # Labels for the bars
    win_rates = [switch_win_rate, stay_win_rate]  # Win rates for each strategy

    plt.bar(labels, win_rates, color=['blue', 'red'])  # Create the bar chart
    plt.ylabel('Win Rate')  # Set the y-axis label
    plt.title(f'Monty Hall Simulation Results ({num_doors} Doors)')  # Set the chart title
    plt.ylim(0, 1)  # Set the y-axis limits to 0-1 (for percentages)
    plt.show()  # Display the chart

def interactive_menu():
    """
    Displays an interactive console menu for running the Monty Hall simulation.
    """
    while True:
        print("\nMonty Hall Simulation Menu")
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
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monty Hall Simulation Script")
    parser.add_argument('-i', '--interactive', action='store_true', help="Run the script in interactive mode")
    args = parser.parse_args()

    if args.interactive:
        interactive_menu()
    else:
        # Default behavior: run the simulation with 3 doors
        run_simulation(3)
import random
import argparse
import matplotlib.pyplot as plt

def monty_hall_simulation(num_trials, switch_doors, num_doors):
    """
    Simulates the Monty Hall problem for a specified number of trials and number of doors.

    Args:
        num_trials (int): The number of times to run the simulation.
        switch_doors (bool): Whether the player switches doors after Monty's reveal.
        num_doors (int): The total number of doors in the game.

    Returns:
        float: The win rate (number of wins / total trials).
    """
    wins = 0  # Initialize the win counter
    for _ in range(num_trials):
        car_door = random.randint(0, num_doors - 1)
        player_choice = random.randint(0, num_doors - 1)

        # Monty reveals a goat behind a door that is NOT the car and NOT the player's choice.
        monty_reveal = random.sample([i for i in range(num_doors) if i != car_door and i != player_choice], num_doors - 2)

        # If the player switches doors:
        if switch_doors:
            remaining_doors = [i for i in range(num_doors) if i != player_choice and i not in monty_reveal]
            player_choice = random.choice(remaining_doors)

        if player_choice == car_door:
            wins += 1

    return wins / num_trials

def run_simulation(num_doors, save_path=None):
    num_trials = 10000
    switch_win_rate = monty_hall_simulation(num_trials, True, num_doors)
    stay_win_rate = monty_hall_simulation(num_trials, False, num_doors)
    
    print(f"Win rate when switching doors ({num_doors} doors): {switch_win_rate:.4f}")
    print(f"Win rate when staying with the original choice ({num_doors} doors): {stay_win_rate:.4f}")
    
    labels = ['Switch Doors', 'Stay with Original Choice']
    win_rates = [switch_win_rate, stay_win_rate]
    
    plt.figure()
    plt.bar(labels, win_rates, color=['blue', 'red'])
    plt.ylabel('Win Rate')
    plt.title(f'Monty Hall Simulation Results\n(Chatgpt 4o) ({num_doors} doors)')
    plt.ylim(0, 1)
    
    if save_path:
        plt.savefig(save_path)
    plt.show()
    plt.close()

def run_all_simulations():
    """Runs all simulations and saves the graphs."""
    images_dir = '/Users/wleon/Dropbox/_Back2Bits/TheMontyHallProblem/images'
    os.makedirs(images_dir, exist_ok=True)
    
    configurations = [
        (3, 'chatgpt_4o_3_doors.jpg'),
        (10, 'chatgpt_4o_10_doors.jpg'),
        (1000, 'chatgpt_4o_1000_doors.jpg')
    ]
    
    for num_doors, filename in configurations:
        save_path = os.path.join(images_dir, filename)
        run_simulation(num_doors, save_path)

def interactive_mode():
    while True:
        print("\nMonty Hall Simulation - Interactive Mode")
        print("1. Run the problem with 3 doors")
        print("2. Run the problem with 10 doors")
        print("3. Run the problem with 1000 doors")
        print("4. Run all simulations")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            run_simulation(3)
        elif choice == '2':
            run_simulation(10)
        elif choice == '3':
            run_simulation(1000)
        elif choice == '4':
            run_all_simulations()
        elif choice == '5':
            print("Exiting interactive mode.")
            break
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monty Hall Simulation Script")
    parser.add_argument("-i", "--interactive", action="store_true", help="Run the script in interactive mode")
    args = parser.parse_args()
    
    if args.interactive:
        interactive_mode()
    else:
        run_simulation(3)
