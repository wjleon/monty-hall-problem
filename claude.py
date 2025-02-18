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
        
        # Monty reveals all but one door (excluding car and player's choice)
        available_doors = set(range(num_doors))
        available_doors.remove(car_door)  # Remove car door
        if player_choice in available_doors:
            available_doors.remove(player_choice)  # Remove player's choice if it's not the car door
            
        # Monty reveals all doors except one (if switching) or none (if staying)
        if switch_doors:
            # Leave one door unopened (besides player's choice)
            remaining_door = None
            if player_choice == car_door:
                # If player chose car, randomly keep one goat door closed
                remaining_door = random.choice(list(available_doors))
            else:
                # If player chose goat, keep car door closed
                remaining_door = car_door
                
            # Switch to the remaining unopened door
            player_choice = remaining_door

        # Check if won
        if player_choice == car_door:
            wins += 1
            
    return wins / num_trials

def run_simulation(num_doors):
    """
    Runs the simulation for a specific number of doors and displays results.
    """
    num_trials = 10000
    switch_win_rate = monty_hall_simulation(num_trials, True, num_doors)
    stay_win_rate = monty_hall_simulation(num_trials, False, num_doors)
    
    print(f"\nResults for {num_doors} doors:")
    print(f"Win rate when switching doors: {switch_win_rate:.4f}")
    print(f"Win rate when staying with the original choice: {stay_win_rate:.4f}")
    
    # Visualize results
    labels = ['Switch Doors', 'Stay with Original Choice']
    win_rates = [switch_win_rate, stay_win_rate]
    plt.figure(figsize=(8, 6))
    plt.bar(labels, win_rates, color=['blue', 'red'])
    plt.ylabel('Win Rate')
    plt.title(f'Monty Hall Simulation Results ({num_doors} doors)')
    plt.ylim(0, 1)
    plt.show()

def interactive_menu():
    """
    Displays an interactive menu for the user to choose simulation options.
    """
    while True:
        print("\nMonty Hall Problem Simulator")
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
    parser = argparse.ArgumentParser(description='Monty Hall Problem Simulator')
    parser.add_argument('-i', '--interactive', action='store_true',
                        help='Run in interactive mode with menu')
    args = parser.parse_args()
    
    if args.interactive:
        interactive_menu()
    else:
        # Default behavior: run with 3 doors
        run_simulation(3)

if __name__ == "__main__":
    main()