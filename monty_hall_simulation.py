"""
Monty Hall Simulation Script

Author: Wilmer Leon
Contact: https://www.linkedin.com/in/wilmer-leon/

Description:
This script simulates the Monty Hall problem, a classic probability puzzle.
It demonstrates the win rates for both switching doors and staying with the
original choice.  The script supports a configurable number of trials and
visualizes the results using matplotlib.

Usage:
Run the script with the following command:
    python monty_hall_simulation.py

Dependencies:
- Python 3.6 or higher
- `random` package (built-in)
- `matplotlib` package (install with `pip install matplotlib`)
"""

import random
import matplotlib.pyplot as plt

def monty_hall_simulation(num_trials, switch_doors):
    """
    Simulates the Monty Hall problem for a specified number of trials.

    Args:
        num_trials (int): The number of times to run the simulation.
        switch_doors (bool): Whether the player switches doors after Monty's reveal.

    Returns:
        float: The win rate (number of wins / total trials).
    """
    wins = 0  # Initialize the win counter
    for _ in range(num_trials):  # Iterate through each trial
        # Randomly assign the car to one of the three doors (0, 1, or 2)
        car_door = random.randint(0, 2)

        # Player makes a random initial choice of doors (0, 1, or 2)
        player_choice = random.randint(0, 2)

        # Monty reveals a goat behind a door that is NOT the car and NOT the player's choice.
        #  - Create a list of possible doors to reveal.
        #  - Exclude the door with the car.
        #  - Exclude the player's chosen door.
        #  - Randomly choose one of the remaining doors to reveal.
        monty_reveal = random.choice([i for i in range(3) if i != car_door and i != player_choice])

        # If the player switches doors:
        #  - Determine the door to switch to.
        #  - It must be different from the player's original choice.
        #  - It must be different from the door Monty revealed.
        if switch_doors:
            player_choice = [i for i in range(3) if i != player_choice and i != monty_reveal][0]

        # Check if the player's final choice (after potentially switching) is the car door.
        if player_choice == car_door:
            wins += 1  # Increment the win counter if the player won.

    return wins / num_trials  # Calculate and return the win rate.

# Run simulations
num_trials = 10000  # Set the number of trials for the simulations
switch_win_rate = monty_hall_simulation(num_trials, True)  # Simulate with switching doors
stay_win_rate = monty_hall_simulation(num_trials, False)  # Simulate without switching doors

# Print the results to the console
print(f"Win rate when switching doors: {switch_win_rate:.4f}")
print(f"Win rate when staying with the original choice: {stay_win_rate:.4f}")

# Visualize the results using a bar chart
labels = ['Switch Doors', 'Stay with Original Choice']  # Labels for the bars
win_rates = [switch_win_rate, stay_win_rate]  # Win rates for each strategy

plt.bar(labels, win_rates, color=['blue', 'red'])  # Create the bar chart
plt.ylabel('Win Rate')  # Set the y-axis label
plt.title('Monty Hall Simulation Results')  # Set the chart title
plt.ylim(0, 1)  # Set the y-axis limits to 0-1 (for percentages)
plt.show()  # Display the chart