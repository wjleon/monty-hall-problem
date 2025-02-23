"""
Monty Hall Simulation Script

Author: Wilmer Leon
Contact: https://www.linkedin.com/in/wilmer-leon/

Description:
This script simulates the Monty Hall problem, a classic probability puzzle.
It demonstrates the win rates for both switching doors and staying with the
original choice. Supports interactive mode with variable door counts.

Usage:
python monty_hall_simulation.py [-i/--interactive]

Dependencies:
- Python 3.6 or higher
- `random` package (built-in)
- `matplotlib` package (install with `pip install matplotlib`)
"""

import random
import matplotlib.pyplot as plt
import argparse

def monty_hall_simulation(num_doors, num_trials, switch_doors):
    """
    Simulates the Monty Hall problem for a specified number of doors and trials.

    Args:
        num_doors (int): Number of doors in the simulation
        num_trials (int): The number of times to run the simulation
        switch_doors (bool): Whether the player switches doors after Monty's reveal

    Returns:
        float: The win rate (number of wins / total trials)
    """
    wins = 0
    for _ in range(num_trials):
        car_door = random.randint(0, num_doors - 1)
        player_choice = random.randint(0, num_doors - 1)
        
        # Monty reveals all but one door, excluding player's choice and car
        available_to_open = [i for i in range(num_doors) if i != car_door and i != player_choice]
        monty_reveals = random.sample(available_to_open, num_doors - 2)
        
        if switch_doors:
            remaining_doors = [i for i in range(num_doors) if i != player_choice and i not in monty_reveals]
            player_choice = remaining_doors[0]
            
        if player_choice == car_door:
            wins += 1
            
    return wins / num_trials

def run_simulation(num_doors, num_trials):
    """Run simulation and display results for given number of doors."""
    switch_win_rate = monty_hall_simulation(num_doors, num_trials, True)
    stay_win_rate = monty_hall_simulation(num_doors, num_trials, False)

    # Print results
    print(f"\nResults for {num_doors} doors ({num_trials} trials):")
    print(f"Win rate when switching doors: {switch_win_rate:.4f}")
    print(f"Win rate when staying with original choice: {stay_win_rate:.4f}")

    # Visualize results
    labels = ['Switch Doors', 'Stay with Original Choice']
    win_rates = [switch_win_rate, stay_win_rate]
    
    plt.bar(labels, win_rates, color=['blue', 'red'])
    plt.ylabel('Win Rate')
    plt.title(f'Monty Hall Simulation Results\n{num_doors} Doors, {num_trials} Trials')
    plt.ylim(0, 1)
    plt.show()

def interactive_menu():
    """Display interactive menu for simulation options."""
    num_trials = 10000  # Default number of trials
    
    while True:
        print("\nMonty Hall Simulation Menu")
        print("1. Run with 3 doors")
        print("2. Run with 10 doors")
        print("3. Run with 1000 doors")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            run_simulation(3, num_trials)
        elif choice == '2':
            run_simulation(10, num_trials)
        elif choice == '3':
            run_simulation(1000, num_trials)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(description="Monty Hall Problem Simulator")
    parser.add_argument('-i', '--interactive', action='store_true',
                       help='Run in interactive mode')
    args = parser.parse_args()
    
    if args.interactive:
        interactive_menu()
    else:
        run_simulation(3, 10000)

if __name__ == "__main__":
    main()