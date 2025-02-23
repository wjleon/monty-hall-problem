"""
Monty Hall Simulation Script

Author: Wilmer Leon
Contact: https://www.linkedin.com/in/wilmer-leon/

Description:
This script simulates the Monty Hall problem, a classic probability puzzle.
It demonstrates the win rates for both switching doors and staying with the
original choice. The script supports a configurable number of trials and
visualizes the results using matplotlib.


Dependencies:
- Python 3.6 or higher
- `random` package (built-in)
- `matplotlib` package (install with `pip install matplotlib`)
- `argparse` package (built-in)
"""

import random
import matplotlib.pyplot as plt
import argparse

def run_simulation(num_doors=3, num_trials=10000):
    """
    Runs the Monty Hall simulation.

    Args:
        num_doors (int): The number of doors in the simulation.
        num_trials (int): The number of trials to run.

    Returns:
        tuple: A tuple containing the win percentages for switching and not switching.
    """
    switch_wins = 0
    stay_wins = 0

    for _ in range(num_trials):
        # Randomly choose the door with the prize
        winning_door = random.randint(0, num_doors - 1)

        # Player makes an initial choice
        player_choice = random.randint(0, num_doors - 1)

        # Host opens a door that is not the winning door and not the player's choice
        available_doors = [i for i in range(num_doors) if i != winning_door and i != player_choice]
        host_choice = random.choice(available_doors)

        # Player switches to the remaining door
        switch_choice = [i for i in range(num_doors) if i != player_choice and i != host_choice][0]

        # Determine if the player won by switching
        if switch_choice == winning_door:
            switch_wins += 1

        # Determine if the player won by staying
        if player_choice == winning_door:
            stay_wins += 1

    # Calculate win percentages
    switch_win_percentage = (switch_wins / num_trials) * 100
    stay_win_percentage = (stay_wins / num_trials) * 100

    return switch_win_percentage, stay_win_percentage


def plot_results(switch_win_percentage, stay_win_percentage, num_doors):
    """
    Plots the results of the Monty Hall simulation.

    Args:
        switch_win_percentage (float): The win percentage for switching.
        stay_win_percentage (float): The win percentage for staying.
        num_doors (int): The number of doors used in the simulation.
    """
    labels = ['Switch', 'Stay']
    win_percentages = [switch_win_percentage, stay_win_percentage]

    plt.bar(labels, win_percentages, color=['blue', 'green'])
    plt.ylabel('Win Percentage')
    plt.title(f'Monty Hall Problem Simulation Results ({num_doors} doors)')
    plt.ylim(0, 100)
    plt.savefig(f'/Users/wleon/Dropbox/_Back2Bits/TheMontyHallProblem/images/vscode_{num_doors}_doors.jpg')
    plt.close()


def main():
    """
    Main function to run the Monty Hall simulation and plot the results.
    """
    parser = argparse.ArgumentParser(description="Simulate the Monty Hall problem.")
    parser.add_argument("-i", "--interactive", action="store_true", help="Run in interactive mode.")
    args = parser.parse_args()

    if args.interactive:
        while True:
            print("\nMonty Hall Problem Simulation")
            print("1. Run with 3 doors")
            print("2. Run with 10 doors")
            print("3. Run with 1000 doors")
            print("4. Run All")
            print("5. Quit")

            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                num_doors = 3
                switch_win_percentage, stay_win_percentage = run_simulation(num_doors=num_doors)

                print(f"\nMonty Hall Simulation Results ({num_doors} doors):")
                print(f"Switching win percentage: {switch_win_percentage:.2f}%")
                print(f"Staying win percentage: {stay_win_percentage:.2f}%")

                plot_results(switch_win_percentage, stay_win_percentage, num_doors)
            elif choice == '2':
                num_doors = 10
                switch_win_percentage, stay_win_percentage = run_simulation(num_doors=num_doors)

                print(f"\nMonty Hall Simulation Results ({num_doors} doors):")
                print(f"Switching win percentage: {switch_win_percentage:.2f}%")
                print(f"Staying win percentage: {stay_win_percentage:.2f}%")

                plot_results(switch_win_percentage, stay_win_percentage,num_doors)
            elif choice == '3':
                num_doors = 1000
                switch_win_percentage, stay_win_percentage = run_simulation(num_doors=num_doors)

                print(f"\nMonty Hall Simulation Results ({num_doors} doors):")
                print(f"Switching win percentage: {switch_win_percentage:.2f}%")
                print(f"Staying win percentage: {stay_win_percentage:.2f}%")

                plot_results(switch_win_percentage, stay_win_percentage,num_doors)
            elif choice == '4':
                doors_options = [3, 10, 1000]
                for num_doors in doors_options:
                    switch_win_percentage, stay_win_percentage = run_simulation(num_doors=num_doors)

                    print(f"\nMonty Hall Simulation Results ({num_doors} doors):")
                    print(f"Switching win percentage: {switch_win_percentage:.2f}%")
                    print(f"Staying win percentage: {stay_win_percentage:.2f}%")

                    plot_results(switch_win_percentage, stay_win_percentage, num_doors)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue
    else:
        switch_win_percentage, stay_win_percentage = run_simulation()

        print("\nMonty Hall Simulation Results (3 doors):")
        print(f"Switching win percentage: {switch_win_percentage:.2f}%")
        print(f"Staying win percentage: {stay_win_percentage:.2f}%")

        plot_results(switch_win_percentage, stay_win_percentage, 3)


if __name__ == "__main__":
    main()