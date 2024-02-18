from random import randint

def get_user_input():
    """Gathers user input for the simulation parameters."""
    number_of_bets = int(input("How many bets would you like to make per day? "))
    days_playing = int(input("How many days would you like to play? "))
    initial_pass_line_bet = float(input("What is your initial pass line bet amount? "))
    return number_of_bets, days_playing, initial_pass_line_bet

def roll_dice():
    """Simulates rolling two dice and returns their sum."""
    return randint(1, 6) + randint(1, 6)

def calculate_odds_bet(point, initial_pass_line_bet):
    """Calculate the odds bet based on the point."""
    if point in [4, 10]:
        return initial_pass_line_bet * 3
    elif point in [5, 9]:
        return initial_pass_line_bet * 4
    elif point in [6, 8]:
        return initial_pass_line_bet * 5

def craps_simulation(number_of_bets, days_playing, initial_pass_line_bet):
    odds_payout = {4: 2, 5: 3/2, 6: 6/5, 8: 6/5, 9: 3/2, 10: 2}
    total_winnings = 0
    dice_rolls = 0
    wins = {"come-out roll wins": 0, "point wins": 0}
    losses = {"come-out roll losses": 0, "point losses": 0}
    daily_winnings = []
    point_rolls_count = []  # Track rolls after point is established

    for day in range(1, days_playing + 1):
        day_winnings = 0
        for bet in range(1, number_of_bets + 1):
            roll_result = roll_dice()
            dice_rolls += 1

            if roll_result in [7, 11]:
                wins["come-out roll wins"] += 1
                day_winnings += initial_pass_line_bet
            elif roll_result in [2, 3, 12]:
                losses["come-out roll losses"] += 1
                day_winnings -= initial_pass_line_bet
            else:
                point = roll_result
                rolls_after_point = 0  # Reset rolls counter for each point established
                odds_bet = calculate_odds_bet(point, initial_pass_line_bet)
                point_roll = roll_dice()
                dice_rolls += 1
                rolls_after_point += 1

                while point_roll not in [7, point]:
                    point_roll = roll_dice()
                    dice_rolls += 1
                    rolls_after_point += 1

                point_rolls_count.append(rolls_after_point)  # Add rolls count to list

                if point_roll == point:
                    wins["point wins"] += 1
                    winnings = initial_pass_line_bet + (odds_bet * odds_payout[point])
                    day_winnings += winnings
                else:
                    losses["point losses"] += 1
                    day_winnings -= (initial_pass_line_bet + odds_bet)
        daily_winnings.append(day_winnings)
        total_winnings += day_winnings

    avg_rolls_after_point = sum(point_rolls_count) / len(point_rolls_count) if point_rolls_count else 0

    return total_winnings, dice_rolls, wins, losses, daily_winnings, avg_rolls_after_point

# Get user input
number_of_bets, days_playing, initial_pass_line_bet = get_user_input()

# Run the simulation
total_winnings, dice_rolls, wins, losses, daily_winnings, avg_rolls_after_point = craps_simulation(number_of_bets, days_playing, initial_pass_line_bet)

# Display the results
print(f"\nTotal winnings after {days_playing} day(s): ${total_winnings}")
print(f"Total dice rolls made: {dice_rolls}")
print("Total wins:", wins)
print("Total losses:", losses)
for day, winnings in enumerate(daily_winnings, start=1):
    print(f"Winnings for Day {day}: ${winnings}")
print(f"Average number of rolls after point is established until resolution: {avg_rolls_after_point:.2f}")
