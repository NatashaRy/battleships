# **Battleships**
## **Site Overview**
The Battleship game is an engaging terminal-based duel between a human player and a computer opponent built in Python. In this classic naval combat game, both players strategically place their fleet of ships, including Battleships, Submarines, and Patrol boats, on a grid. Once the ships are set, the players take turns guessing the location of their opponent's vessels. 

The game provides real-time feedback, updating the board to show hits and misses, and informing players when they've struck or sunk an adversary's ship. The computer opponent, not just relying on random guesses, adapts its strategy if it scores a hit, targeting nearby cells in a more calculated manner. Gameplay continues until one player successfully sinks all of the opponent's ships. With clear visual representations, input validations, and the option to replay, this Battleship rendition offers a comprehensive and immersive experience right in the terminal.
​
![Am I responsive screenshot](imagelocation so maybe docs/image.jpg)
​
## Table of contents:
1. [**Site Overview**](#site-overview)
1. [**Planning stage**](#planning-stage)
    * [***Target Audiences***](#target-audiences)
    * [***User Stories***](#user-stories)
    * [***Site Aims***](#site-aims)
1. [**How to play**](#how-to-play)
1. [**Features**](#features)
    * [***Future Enhancements***](#future-enhancements)
1. [**Data Model**](#data-model)
1. [**Future-Enhancements**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
    * [***Bugs***](#bugs)
1. [**Deployment**](#deployment)
1. [**Tech**](#tech)
1. [**Libraries**](#libraries)
1. [**Software**](#credits)
    * [**Honorable mentions**](#honorable-mentions)
    * [**General reference**](#general-reference)
    * [**Content**](#content)
​
## **Planning stage**
### **Target Audiences:**​
* People who like to play Battleships game. 
* People who enjoy strategic board games.
* People who prefer turn-based games over real-time games. 
* People looking for a quick and engaging game during short breaks.
​

### **User Stories:**
* As a user, I want to be able to place my own ships on the game board.
* As a user, I want to input my guesses easily with as few clicks as possible.
* As a user, I want to know when my ships are hit or sunk. 
* As a user, I want to see the entrie game board, so I can strategize my next move. 
* As a user, I want be able to restart the game quickly if I wish to play again.


### **Site Aims:**
* Introduce userst to the basics of strategy games and logical thinking.
* Proivde an interactive platform for users to play Battleships online.
* Offer a user-friendly interface. 
* Ensure the game is playable without requering any special packages or installations.
​

## **How to play:**

​
* To inform the user on opening times
* To inform the user about what we offer when they are here
* To offer the user an oppertunity to get in contact

## **Features**

**1. Two player game**
* The game is designed for two players: the human player and the computer opponent. 

**2. Interactive ship placement**
* Users manually place their ships on the board.
* Choosing both the starting position and orientation (horizontal or vertical).

**3. Randomize computer ship placement**
* The computer opponent places its ships on the board randomly at the start of each game.

**4. Guessing mechanism**
* Players take turns guessing the location of the opponent's ships on the board.
* The game provides feedback on whether a guess results in a hit or miss.


**Data Model**

**Accepts user input**
    * Users name
    * Row and column in format e.g. 'A1'

**Different types of ships**
    * Three different types of ships
    * Marked with first character of ships name on board

**Generating random board**
    * Ships are randomly placed for the computer
    * Player can not see placement of computers ships

**Let player place ships on board**
    * Player choses start position, row and column for the ships
    * Player chooses which orientation the ship should have

* Play against computer
    *

* Input validation
    * Check that the input is in correct format e.g. 'A1'
    * Player or computer can not make the same guess twice
    * Ships can not be placed outside of the board

* Play again och quit
    * Player can choose to play again
    * Game restarts automatically where player place ships

​
### **Future-Enhancements**
* Adding player vs player option.
* Adding a scoreboard both in the beginning and end to show improved performance,
* Choose size of board and number of ships.
* Option to chose limited turns and time.
​
## **Testing Phase**
We have tested the game simultaneously througout development. Every function has been tested independently aswell when running the program. Tests are described below and if bugs were found they are described under [Bugs](#bugs) .

### **Functionality**
#### **Valid input from user**
The user makes several inputs playing the game, each input has been tested independently and ll works as expected.

##### **1. Input from user**
* **Name of player**
    * **Description:** When starting the game, the player need to enter it name to be able to continue. The input is limited to only letters. 
    * **Tests:** 
        * 1. We have tested to enter a name several times and continue the game.
        * 2. We have tested to enter numbers in the input, the game asked us to enter our name with letters only.
    * **Result:** Works as expected.
 

* **Row and column for placing ships**
    * **Description:** The user is placeing the ships by choosing a starting position in format column + row ('A1', letter + number), and the enter if the orientation is horizontal ('H') or vertical ('V').
    * **Tests:**
        * Starting position
            * 1. Input with correct format - A1, works as expected.
            * 2. Input with incorrect format - Only letters, error message appears.
            * 3. Input with incorrect format - Only number, error message appears.
            * 4. Input with incorrect format - Only number or letter, error message appears.
            * 5. Input with incorrect format - To long input two letters + number, error message appears.
            * 6. Input with incorrect format - To long input one letters + two number, error message appears.
            Error message appearing: *"Please enter starting position for Battleship (e.g., A1):"*

        * Orientation
            * 5. Input in correct format - 'H' for horizontal orientation, works as expected. 
            * 6. Input in correct format - 'V' for vertical orientation, works as expected
            * 7. Input with incorrect format - One letter, error message appears.
            * 8. Input with incorrect format - Three letters, error message appears.
            * 9. Input with incorrect format - One number, error message appears.
            * 10. Input with incorrect format - Number + letter, error message appears.
            Error message appearing: *Invalid orientation. Choose 'H' or 'V'. Enter orientation (H for horizontal, V for vertical):*
    * **Result:** Works as expected.


* **Row and column for guess**
    * **Description:** When user makes a guess the format is limited to column + row ('A1'), before we started testing we realized that the format was the opposite of the the ship placement ('1A'), more described under [Bugs](#bugs). This to make the inputs less confusing for the user. 
    * **Test:**
        * 1. Input with correct format - A1, works as expected.
        * 2. Input with incorrect format - Only letters, error message appears.
        * 3. Input with incorrect format - Only number, error message appears.
        * 4. Input with incorrect format - Only number or letter, error message appears.
        * 5. Input with incorrect format - To long input two letters + number, error message appears.
        * 6. Input with incorrect format - To long input one letters + two number, error message appears.
        Error message: *"Invalid input. Please enter your guess (e.g., '1A', '2B'):"*
    * **Result:** Works as expected.

* **Restart game**
    * **Description:** When game ends the player can choose to restart the game by usin "Y" for yes and any other key for no.
    * **Test:**
        * 1. Input "Y" - The game is restarted.
        * 2. Input any other key - The game thanks the player and says goodbye.
    * **Result:** Works as expected.


##### **2. Clear terminal**
**Description:** The terminal clears after entering name
**Test:**
* Testing if the terminal clears when continue the game after entering name. 
**Result:** Works as expected.

##### **3. Validation for ships placement**
**Description:** The user chose where the place the ships on the board by entering starting position and orientation. The game checks is there already is an other ship placed in the chosen cells and that the ships placement is inside the board. Prints messages when all ships are placed on board.

**Tests:**
* 1. Valid placement - Starting position ('A1') and orientation ('H'), the ship is being placed marked with the first character of the ships name.
* 2. Invalid placement - On already placed ship, error message appears.
Error message: *"Another ship is already in that position."*
* 3. Invalid placement - Outside of board (tested both horizontal and veritcal) , error message appears.
Error message: *"Ship placement out of bounds, try again."*
* 4. Valid placement fpr all ships - Sucess message printed *"All ships have been successfully placed!*
**Result:** Works as expected.

##### **4. Delay** 
**Description:** The terminal add a delay when user placed ships, between guesses, before restart option appears

**Test:** When playing the game we tried to change the time in `time.sleep()` function to see if it the delayed time changed and deciding what would be a suitable for delay, ending up with 1 second.

* **Result:** Work as expected.


##### **5. User hits, misses, sunk ship and secound guesses**
**Description:** When a user hits one of the computes ships, it is marked on the board with the first character of the ships name and a miss is marked with an 'X'.

**Test:**
* 1. Input guess that hit ship, when hit, first character of ship name appears on game board and prints messege telling the user which ship was hit. 
Message: *"You hit the  [Name of ship]!"*
* 2. Input guess that misses ship, marked with '×' on game board and a message telling the user it missed.
* 3. Input guess for hit placement, error message appears.
* 4. Input guess for missed placement, error message appears.
Error message: *"You already guessed that, try again."*
* 5. Messeges prints when the user sinks a ship. 
Message: *"You have sunk the computers [Name of ship]!"*

**Result:** We found a bug described in [Bug](#bugs). After solving the issues it works as expected.


##### **6. Computer hits, misses, sunk ships and next guess**
**Description:** When the computer hit one of the playes ships, the first character of the ship is changed to '×' and a miss is marked with an '⁑'.

* 1. Computer hits ship, first character of ship name changes to '×' on players board, print message telling user computer hit ship appears.
* 2. Computer misses ship, marked with '⁑' on game board and print message telling the user the computer missed.
* 3. Messeges prints when the computer sinks a ship.
Message: *"The computer has sunk your [Name of ship]!"*
* 4. When the computer hits a ship but not sink it, the next guess should be in the nearby area, we have tested this by printing the next guess in the terminal.

**Result:** Works as expected.

### **Validators**
**PEP8 Online Validator**
Results showed 9 errors, "E501 line too long".
* Line 244, 246, 248: are related to the check the next guess for the computer in relation to the last hit. When trying to split the line, the function does not work as expected. So we have decided not to make any changes.
* Line 398-403: are all related to the ASCII art which is used on the start screen. This error does not affect the functionality of the game while contributing to a better experience for the user.



### **Bugs**
#### **During development**
1. **Input of row and column**
    * Issue - During development we realised that the formatting of input for row and column differed between when the player would add ships (e.g. 'A1') and make guesses (e.g. '1A'). 
    * Resolution - To fix this we changed the order of the valid pattern, so the letter would come first and the number after instead of the opposite that it was from the start.
 

2. **Computers guess**
    * Issue - When adding the function to make the computer guess the placement of the players ships we realised that the computer only was checking the location of the players guess on the `HIDDEN_BOARD`, not actually guessing the the location of the playes ships on the `PLAYERS_BOARD`.
    * Resolution: We change `row` and `column` to `computer_row` and `computer_column` when calling the `computer_guess` function to capture the values of the computer's guess and update the `PLAYERS_BOARD` accordingly.
 

3. **Player could not guess again on repeat guess**
    * Issue - When the player tried to guess at the same place a previous guess was made, the game asked the player to try again while the code continued, preventing the player from making another guess until the next round. 
    * Resolution - By adding a `continue` statement we ensure the player would get a new try before the computer made its guess.
 

4. **Count sunk ships and print what ship have been sunk**
    During development we got encountered with several issues when trying to count the sunken ships before we could find a solution that fitted our needs and wishes. The main problem was that the counter for the player would interfere with the counter for computer, and vice versa.

    * Issues
        - The computer won after making it's first move.
        - The counter would only count each ship one time per a round e.g. if the player sunk the computers Battleship, it would not be counted when the computer would sink the players Battleship and so on.
        - When counting the characters of the ships compared to size the computes ships would not be counted accuratly. 
        - When adding counting "X" to the function, since the computers hits become "X" on the `char`, the players ships would not be counted accurately.

    * Resolution - By not refactoring the function and moving the separate logic into the players and computers turn logic, the problem was solved and behaves as expected.

5. **Check if cell already been guessed**
    During development testing we realized the error message for guessing the same cell twice did not appear if the user had a hit in the perticular cell.

    * Issue - User could guess same cell twice without the game warning and the computer continued guessing which led to the user getting fewer guesses than the computer.
    * Resolution - By creating a variable `ship_chars` that iterates over the values of the `SHIPS` dictionary and adding it to the validation method checking if the cell already been guessed we could solve the problem.
​
***
## **Deployment**
This project was deployed to Heroku through the following process:

### **Setting up app**
1. Log in to [Heroku.com](https://heroku.com)
2. Clicked the button labeled **"New"** on the dashboard in the top right corner under the profile picture.
3. Chooseing **"Create new app"** from the dropdown menu.
4. Enter a **unique** name, we chose ***btlships*** since "Battleships" was already taken.
5. Chose a region, we chose Europe since it is the most relevant.
6. Click button labeled **"Create app"** and come to the projects **"Deploy"** tab.

### **Settings tab**
7. Click the **"Settings"** tab and navigate to **"config Vars"** section.
8. Added **`PORT`** as and **`8000`** as value, then clicked **"add"**.
9. Scroll down to **"Buildpacks"** section, clicking **"Add buildpack"** and then selection **"Python"**.
10. Repeating the process above but adding **"Node.js"** instead of "Python".

### **Deplay tab**
11. Click **"Deploy"** in the tabs menu.
12. Chose **GitHub** as **"Deployment method"**.
13. Comfirm connection. 
14. Search for the repository name and click **"Connect"**. 
15. Chose **"Automatic deploys"** or **"Manual deploys"**.

​
## **Tech**
* Python

## **Libraries**
* Random - Used to generate random place computers ships and for computer guesses. 
* RE - Used to check valid input pattern of users guesses.
* SYS - Exit the game if the user do not wish to play again.
* OS - Used to clear terminal so the user have a clearer view of the game.
* Time - Used to delay the computer's guess so that the user can easily follow along.

## **Software**
* VS Code to create, load and push my code to GitHub.
* [patorjk.com](https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Battleships) for ASCII art.
​
## **Credits**
### **Honorable mentions**
* Richard Wells, my mentor, who is always very supportive and helpful. This project would not be possible without the help I got to clear things out and 
​
### **Genral references:**
* All code is written by myself. 
* I have used [ChatGPT](https://openai.com) when I got stuck and could not figure out how to get forward. I have not asked ChatGPT to write code for me without contributing my own code to be fixed. 

### **Content:**
* Introduction, winner and loser ASCII art graphics from [patorjk.com](https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=Battleships)
​
