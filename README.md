# Bowling Scoring Challenge

## Files included
Here is an overview of the files included in the project
### HTML files:
  * form.html - accepts user input (contains some example inputs)
  * index.html - displays the scoreboard of the input
  * err.html - only displayed if proper input is not provided
### Python files:
  * Bowling.py - handles the score calculation (can also be run independently using inputs from Inputs.txt)
  * main.py - uses Bowling.py to calculate scores and display scores after handling few edge cases
  * BowlingTest.py - contains unit tests for the project (uses Inputs.txt file for inputs)
### Input file:
  * Inputs.txt - used solely by BowlingTest.py (but can also be used by other files if required)

##Input
The system accepts inputs from the User or Inputs.txt in the following formats:
  * list of integers - include '[]' for input list.
  * list of integers and strings  - include '[]' for input list (Strike: X, Spare: /, Missed: -)
  
For example:
  
Input: Strike, 7, Spare, 9, Miss, Strike, Miss, 8, 8, Spare, Miss, 6, Strike, Strike, Strike, 8, 1 
  
Given Input would be: 
    
    [10, 7, 3, 9, 0, 10, 0, 8, 8, 2, 0, 6, 10, 10, 10, 8, 1] or [X, 7, /, 9, 0, X, 0, 8, 8, /, 0, 6, X, X, X, 8, 1]

## Scoreboard
* The board consists of 4 columns (FrameID, Roll1, Roll2, Roll3, Total) and 10 rows. 
* Strikes are denoted by 10
* Misses are denoted by 0
* Spares are denoted by 10 - previous roll
* Final Score of game is the last cell of the 10th frame

## Data Model
### Bowling.py
This contains the BowlingChallenge class:
* convertStringstoInt() - Converts list of inputs to integers
* readInput() - Used if Input is being read from the Inputs.txt file. Uses convertStringstoInt()
* bowling_score() - Main score calculator for the project. Accepts input from main.py
### main.py
* form() - Accepts input list from user, converts it to integers (uses convertStringstoInt()) and displays the scoreboard (uses bowling_score()). Uses the HTML files for rendering output.
* add_header() - Used to add headers to the form() response if required. (E.g. Cache-Control)

## Logic
* Each row is a new frame and can roll/throw 2 times (Roll1 and Roll2) and Roll3 is always "None" if frame number is not 10.
* If roll/throw is a Strike (input = 10) and frame is not 10, then Roll2 is assigned as "None", and the input for the next frame considered. Score is 10 + Curr_frame+1_roll1 + Curr_frame+1_roll2
* If roll/throw is a Strike or Spare, and it is the last frame (frame=10), then Roll3 is considered while calculating the final score of the game.
* If roll/throw is a Spare, and frame is not 10, the score is 10 + Curr_frame_roll + Curr_frame+1_roll1
* If anything other than a Spare or Strike is rolled, Score is CumulativeSum + roll

## Executing the code
The project uses a very simple API to accept the inputs and display the scores.

To execute the code:
  * Run main.py
  * Redirect to http://localhost:5000/ on the browser (I have used Chrome and Edge).
  * Provide the input in list of integers form as mentioned above.
  * If the input is correct, the scoreboard is displayed.
  * The user can use the link provided at the bottom of the scoreboard to play a new game.
  * If the input is wrong, an error message is displayed, and the user can go back to the input page using the link provided.

## Handled Edge Cases:
 * Total number of rolls/throws per game should always be <= 21
 * Total score per game must be <= 300
 * If a game has all Strikes, then number of rolls/throws cannot exceed 12
 * A game cannot be less than 10 frames
 * A game cannot exceed 10 frames (used brute force in this situation due to time constraints)

## Test cases
There are 8 test cases included in this project. All the inputs required for the following tests are available in Inputs.txt:
* Test 1: Challenge input (Input: List of Integers)
* Test 2: Challenge input (Input: List of Integers and Strings)
* Test 3: Input with a Spare in the Tenth frame (Input: List of Integers)
* Test 4: Input with a NO Spares or Strikes in the Tenth frame (Input: List of Integers)
* Test 5: Input with all Strikes (Input: List of Integers)
* Test 6: Input with a Single Strike (Input: List of Integers)
* Test 7: Input taken from a real game (Input: List of Integers)
* Test 8: Input taken from a real game with a Spare in the Tenth frame (Input: List of Integers)

## Creating the system:
The process of creating this system was interesting due to the unfamiliarity of the scoring system in bowling.

At first, I tried treating each input as a [key, val] pair but realised that it would be difficult to handle all the edge and test cases that I would definitely want to incorporate within the given time. 

I started with a basic algorithm for a single frame score based on the rules of the game. Extending the same logic to other frames, required the use of a list of dictionaries. The pseudocode of the logic is given below:   
```python
scoreList = []
frame1Dict = {'frameID':1, 'roll1': 7, 'roll2': 3, 'roll3': None, 'total': 10}
scoreList.append(frame1Dict)
```
The total score of any frame is the cumulative sum of the frameScores till that particular frame.

I included the ability to independently run and debug the Bowling.py in order to make the code execution and readability as smooth as possible.

## Further Enhancements and known shortcomings:
  * Inputs of each game to be taken one at a time:
    As mentioned earlier, I tried treating each input as a dictionary entry to address this aspect, but decided against it due to lack of time. I did not want to sacrifice the logic aspect of the system.
  * Strike frame total does not display 10 + [roll + 1] + [roll + 2] on the table. This does not affect the final score of the game.
  * Exit from execution can be handled using Flask threads and WebSockets:
    Currently, the execution can only be stopped if you stop running main.py. This returns an exit code of -1 


