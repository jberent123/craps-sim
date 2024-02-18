from random import randint
#lets find a way to make this work using your brian!!

def roll_dice():
    """Simulate rolling two dice."""
    return randint(1, 6) + randint(1, 6)

def calculate_odds_bet(point, pass_line_bet, bankroll):
    """Calculate the odds bet based on the point, constrained by remaining bankroll."""
    if point in [4, 10]:
        return pass_line_bet * 3 if pass_line_bet * 3 <= bankroll else bankroll
    elif point in [5, 9]:
        return pass_line_bet * 4 if pass_line_bet * 4 <= bankroll else bankroll
    elif point in [6, 8]:
        return pass_line_bet * 5 if pass_line_bet * 5 <= bankroll else bankroll
    return 0

def calculate_payout(point, odds_bet):
    """Calculate the payout for an odds bet."""
    payout_ratios = {4: 2, 5: 3/2, 6: 6/5, 8: 6/5, 9: 3/2, 10: 2}
    return odds_bet * payout_ratios.get(point, 0)

def craps_simulation(bets_per_day, days, initial_bankroll, base_pass_line_bet):
    bankroll = initial_bankroll
    total_rolls = 0
    wins = {"come-out roll wins": 0, "point wins": 0}
    losses = {"come-out roll losses": 0, "point losses": 0}
    largest_pass_line_bet = base_pass_line_bet
    total_bets = 0

    for _ in range(days):
        bets_today = 0
        while bets_today < bets_per_day and bankroll > 0:
            total_bets += 1  # Increment the counter at the start of each bet
            current_pass_line_bet = min(base_pass_line_bet, bankroll)  # Ensure bet does not exceed bankroll
            bankroll -= current_pass_line_bet
            roll = roll_dice()
            total_rolls += 1

            if roll in [7, 11]:  # Come-out roll wins
                bankroll += current_pass_line_bet * 2
                wins["come-out roll wins"] += 1
            elif roll in [2, 3, 12]:  # Come-out roll losses
                losses["come-out roll losses"] += 1
                current_pass_line_bet = min(current_pass_line_bet * 2, bankroll)
            else:  # Point is established
                point = roll
                odds_bet = calculate_odds_bet(point, current_pass_line_bet, bankroll)
                bankroll -= odds_bet
                point_roll = roll_dice()
                total_rolls += 1

                while point_roll not in [7, point]:  # Rolling for point
                    point_roll = roll_dice()
                    total_rolls += 1

                if point_roll == point:  # Point wins
                    bankroll += current_pass_line_bet * 2
                    bankroll += calculate_payout(point, odds_bet) + odds_bet
                    wins["point wins"] += 1
                else:  # 7 out, point losses
                    losses["point losses"] += 1
                    current_pass_line_bet = min(current_pass_line_bet * 2, bankroll)

            largest_pass_line_bet = max(largest_pass_line_bet, current_pass_line_bet)
            bets_today += 1  # Ensure this is correctly incremented after each full betting cycle

    #return bankroll, wins, losses, total_rolls, largest_pass_line_bet
    return bankroll, wins, losses, total_rolls, largest_pass_line_bet, bets_today, total_bets
#why not return bets_today?
#lets try it.  1 Change.  nice!  When I changed it, it automatically added bets_today and total_bets
# Rest of the code remains the same as provided.
def calculate_average_bankroll(simulation_results):
    total_bankroll = sum(result[0] for result in simulation_results)
    return total_bankroll / len(simulation_results)

def main():
    while True:
        num_simulations = int(input("How many simulations would you like to run? (Enter 0 to exit): "))
        if num_simulations == 0:
            break

        bets_per_day = int(input("How many bets per day is the limit? "))  # Prompting the user for this value
        days = 1  # Or prompt the user for this
        initial_bankroll = 1155  # Or prompt the user for this
        base_pass_line_bet = 25  # Or prompt the user for this

        simulation_results = []
        for _ in range(num_simulations):
            result = craps_simulation(bets_per_day, days, initial_bankroll, base_pass_line_bet)
            simulation_results.append(result)

        # Display results and calculate the average ending bankroll
       # for i, (final_bankroll, total_wins, total_losses, total_rolls, largest_bet) in enumerate(simulation_results, start=1):
        for i, (final_bankroll, total_wins, total_losses, total_rolls, largest_bet, bets_today, total_bets) in enumerate(simulation_results, start=1):
            print(f"Simulation Run {i}:")
            print(f"  Final Bankroll: ${final_bankroll}")
            print(f"  Total Wins: {total_wins}")
            print(f"  Total Losses: {total_losses}")
            print(f"  Total Rolls: {total_rolls}")
            print(f"  Largest Pass Line Bet: ${largest_bet}")
            #print(f"  Bets Today: {bets_today}")  # New line to print bets_today since this isnt' accurate
            print(f"  Total Bets: {total_bets}\n")  # New line to print total_bets

            # print(f"Simulation Run {i}:")
            # print(f"  Final Bankroll: ${final_bankroll}")
            # print(f"  Total Wins: {total_wins}")
            # print(f"  Total Losses: {total_losses}")
            # print(f"  Total Rolls: {total_rolls}")
            # print(f"  Largest Pass Line Bet: ${largest_bet}\n")

        average_bankroll = calculate_average_bankroll(simulation_results)
        print(f"\nAverage Ending Bankroll after {len(simulation_results)} simulations: ${average_bankroll:.2f}")

        # Reminder of original inputs
        print("\nReminder of Original Inputs:")
        print(f"Pass Line Bet: ${base_pass_line_bet}")
        print(f"Starting Bankroll: ${initial_bankroll}")
        print(f"Number of Bets per Day: {bets_per_day}\n")

if __name__ == "__main__":
    main()
