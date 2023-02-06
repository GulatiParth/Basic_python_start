#
# Author: Parth Gulati
# Student Number: 131697211
#
# Place the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Parth Gulati
# Student Number: 131697211
#

# Function to determine the winner in a game of Rock-Paper-Scissors
def wins_rock_scissors_paper(player, opponent):
    # ret is a boolean value that stores the result of the game
    ret = True
    
    # If the player and opponent have the same choice, the game is a draw
    if player.lower() == opponent.lower():
        ret = False
    # Check if the player chose rock
    elif player.lower() == "rock":
        if opponent.lower() == "scissors":
            ret = True  
        else:
            ret = False
    # Check if the player chose paper
    elif player.lower() == "paper":
        if opponent.lower() == "rock":
            ret = True  
        else:
            ret = False
    # Check if the player chose scissors
    elif player.lower() == "scissors":
        if opponent.lower() == "paper":
            ret = True  
        else:
            ret = False
    # Return the result of the game
    return ret

# Function to calculate the factorial of a given integer
def factorial(f):
    # Initialize a variable to store the factorial result
    fact = 1
    # Loop through all numbers from 1 to f
    for i in range(1 , f + 1):
        # Multiply the previous result with the current number
        fact = fact * i
    # Return the result
    return fact

# Function to calculate the nth Fibonacci number
def fibonacci(n):
    # Initialize the first two numbers in the sequence
    f = 0
    s = 1
    sm = 0
    # If n is 1, return 1
    if n == 1:
        sm = 1
    # Loop through the range from 0 to n-1
    for i in range(0,n-1):
        # Sum the previous two numbers
        sm = f + s
        # Shift the values to the right
        f = s
        s = sm
    # Return the result
    return sm

# Function to find two elements in an array that add up to a given goal
def sum_to_goal(myArray, goal):
    # Initialize a variable to store the result
    pro = 0
    # Loop through the first element of the array
    for f in myArray:
        # If a pair is already found, break the loop
        if pro != 0:
            break
        # Loop through the second element of the array
        for s in myArray:
            # If the sum of the two elements is equal to the goal, store their product in the result variable
            if (f + s) == goal:
                pro = f * s
                break            
    # Return the result
    return pro

class UpCounter:
    stepSize = 1  # default step size
    counter = 0    # current counter value
    
    def __init__(self, step):
        self.stepSize = step
        
    def count(self):
        return self.counter
        
    def update(self):
        self.counter += self.stepSize  # increase the counter by stepSize

class DownCounter:
    stepSize = 1  # default step size
    counter = 0    # current counter value
    
    def __init__(self, step):
        self.stepSize = step
        
    def count(self):
        return self.counter
        
    def update(self):
        self.counter -= self.stepSize  # decrease the counter by stepSize