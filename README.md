Fruit Hunt Slot Machine Simulator

Author: George Demirjian

Language: Python

Libraries: Pygame, random


Project Overview:

The Fruit Hunt Slot Machine Simulator is a personal project built using Python and Pygame. This game simulates a traditional slot machine with various features such as spinning reels, animations, menu navigation, sound effects, and user interactions. It incorporates object-oriented programming principles to manage the game's components.

Features
Interactive User Interface:

A main menu screen with clear instructions for starting the game.
Spinning reels with animations created using movement per change in time.
Imbedded audio for background music and win notifications.

Gameplay Mechanics:

Reels spin and stop sequentially, revealing symbols that determine the outcome.
Players can place bets and win based on combinations of symbols across the reels.
Player balance updates dynamically based on bet size and wins.

Custom Graphics and Sound:

Custom images are used for symbols on the reels and the background, which were created with image editing software.
Background music loops continuously.

Installation:

Clone this repository to your local machine using the following command: "git clone <https://github.com/georgedemirjian/Personal-Projects.git>". Ensure you have Python installed, then install the required libraries using command "pip install pygame" Change to the Fruit_Hunt_Slots directory and run the main game file by using command "cd Fruit_Hunt_Slots" and then "python3 main.py"

Project Structure:

main.py                # Main game loop and initialization

machine.py             # Handles the slot machine logic

reel.py                # Defines the reel behavior and animations

player.py              # Manages player interactions like balance and bets

ui.py                  # Handles the UI elements like balance, bet size, and win display

settings.py            # Contains global settings such as dimensions and file paths

aesthetics/            # Contains images, fonts, and audio files used in the game


How to Play:


Upon running the game, you will be greeted with a menu screen. Press the Spacebar to begin.
Use the Spacebar to spin the reels. Each spin deducts a fixed amount from your balance as a wager.
The game checks for winning combinations across rows and columns of symbols. Winnings are calculated based on the length of the symbol streak and the wager size. Minimum 3 in a row are required for a win.
The game continues as long as the player has enough balance to wager.


Future Improvements:

Enhancing Gameplay: Add more features like adjustable bet sizes.
Visual Enhancements: Implement more dynamic animations for wins.
