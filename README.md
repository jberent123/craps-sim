# craps-sim

Simulate the best way to bet in craps.

## Overview

This craps simulation is designed to model the game of craps with a focus on betting strategies, specifically implementing the Martingale betting strategy for the pass line bet. The simulation runs a user-defined number of bets per day over a specified number of days, tracks wins and losses, and calculates the largest pass line bet needed due to consecutive losses.

## Features

- **Martingale Strategy Implementation**: Doubles the pass line bet after a loss and resets to the original bet after a win.
- **Odds Bet Calculation**: Calculates the odds bet based on the point, adhering to craps rules (3x for 4 and 10, 4x for 5 and 9, and 5x for 6 and 8).
- **Bankroll Management**: Ensures that bets do not exceed the available bankroll and tracks the largest pass line bet required.
- **Simulation Results**: Provides detailed outcomes, including the final bankroll, total wins and losses, total dice rolls, and the largest pass line bet made.

## Usage

To run the simulation, ensure you have Python installed on your system. Clone this repository and navigate to the project directory. Run the simulation script with:

```bash
python craps_simulation.py

Follow the on-screen prompts to input the number of bets per day, the number of days you want to run the simulation, and your initial bankroll and pass line bet amount.

Customization
The simulation can be customized by adjusting the parameters prompted at runtime:

bets_per_day: The number of bets placed each day.
days: The total number of days to simulate.
initial_bankroll: The starting bankroll for the simulation.
base_pass_line_bet: The initial bet amount for the pass line bet.
Results
After running the simulation, you will receive a summary of the outcomes, including:

Final bankroll after the simulation.
Total wins and losses.
The total number of dice rolls made.
The largest pass line bet required due to consecutive losses.
Contributing
Contributions to this project are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

License
This project is open-sourced under the MIT License. See the LICENSE file for more details.
