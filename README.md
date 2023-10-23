![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome USER_NAME,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

# **Battleships**
## **Site Overview**
XXXXXXXXXXXXXXXXXXXXXXXXX
​
![Am I responsive screenshot](imagelocation so maybe docs/image.jpg)
​
## Table of contents:
1. [**Site Overview**](#site-overview)
1. [**Planning stage**](#planning-stage)
    * [***Target Audiences***](#target-audiences)
    * [***User Stories***](#user-stories)
1. [**How to play**](#how-to-play)
1. [**Features**](#features)
    * [***Existing features***](#existing-features)
    * [***Future Enhancements***](#future-enhancements)
1. [**Data Model**](#data-model)
1. [**Future-Enhancements**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
    * [***Bugs***](#bugs)
1. [**Deployment**](#deployment)
1. [**Tech**](#tech)
1. [**Credits**](#credits)
    * [**Honorable mentions**](#honorable-mentions)
    * [**General reference**](#general-reference)
    * [**Content**](#content)
​
## **Planning stage**
### **Target Audiences:**
​
This section is a breakdown of the target audience 3 or 4 bullet points so using our example
​
* Users interested in retro gaming 
* Users interested in a safe environment to gather and have fun
* Users interested in activities in the Sheffield area
​
### **User Stories:**
​
User stories are more what the user wants from the site in terms of features and presentation
​
* As a user, I want to see the subject matter of the page.
* As a user, I want to navigate the page to find what I require quickly and easily.
* As a user, I want to learn more about what the business offers
* As a user, I want to reach out and contact the business
​
## **How to play:**
​
This is optional but offers the insight into what the aim of the project are
​
* To inform the user on opening times
* To inform the user about what we offer when they are here
* To offer the user an oppertunity to get in contact


## **Data Model**
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
​
​
## **Features**
* Accepts user input
    * Users name
    * Row and column in format e.g. 'A1'

* Different types of ships
    * Three different types of ships
    * Marked with first character of ships name on board

* Generating random board
    * Ships are randomly placed for the computer
    * Player can not see placement of computers ships

* Let player place ships on board
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

### **Existing features**

* This is where you will place all of your features think about each section of the page include a screenshot and a few bullet points on how it's presented and why
​
### **Future-Enhancements**
​
* Scoreboard.
* Choose size of board and number of ships.
* Limited turns and timer.
​
## **Testing Phase**
We have tested the game simultaneously througout development. Every function has been tested independently aswell when running the program. This to make sure that the functionality is working correctly as expected.
​

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

​
***
## **Deployment**
I deployed the page on GitHub pages via the following procedure: -
​
1. From the project's [https://github.com/NatashaRy/battleships](pageurl), go to the **Settings** tab.
2. From the left-hand menu, select the **Pages** tab.
3. Under the **Source** section, select the **Main** branch from the drop-down menu and click **Save**.
4. A message will be displayed to indicate a successful deployment to GitHub pages and provide the live link.
​
You  can find the live site via the following URL - [live webpage](https://yoururlhere)
***
​
## **Tech**
​- Python
​
## **Credits**
### **Honorable mentions**
​
It's always nice to mention those that helped you get there, if people gave you support on slack or the local cat scared you into completing give them a mention!
​
### **Genral references:**
XXXXXXXXXXXXXXXXXXXXXX

### **Content:**
​
If you took any code from online source and by this i mean copy paste with zero changes mention it here!
