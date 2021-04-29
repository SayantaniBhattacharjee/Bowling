from flask import Flask, render_template, request
from ast import literal_eval
from Bowling import BowlingChallenge

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def getInput():


    if request.method == "POST":
        projectpath = request.form['projectFilepath']
    # file containing lists of input scores


        _filename = 'C:/Users/sayan/PycharmProjects/Bowling/Inputs.txt'

        bowl = BowlingChallenge()
        giveninputScores = bowl.readInput(_filename)
        allStrikes = False

        # To change the input list change the keyName on line 23 e.g. 'givenInput' to 'allStrikeInput'
        #inputRolls = giveninputScores['givenInput']

        inputRolls = literal_eval(projectpath)

        if ((len(inputRolls) <= 21)):
            finalScore, table = bowl.bowling_score(inputRolls)

            # Set allStrikes flag to True if all elements of input list are 10
            if all(elem == 10 for elem in inputRolls):
                allStrikes = True

            # Show output only if 0<=finalScore<=300 and table is not empty and (allStrikes is False or allStrikes is True and number of rolls is 12)
            if (0 <= finalScore <= 300 and (allStrikes is True and len(inputRolls) == 12) and len(table) != 0) or (
                    0 <= finalScore <= 300 and allStrikes is False and len(table) != 0):
                print(table)
                return render_template('index.html', title='Bowling Scoreboard', result=table)

            # Error if allStrikes is True and number of inputs > 12
            elif (len(inputRolls) > 12 and allStrikes is True) or finalScore == 0:
                return render_template('err.html')
            else:
                return render_template('err.html')
        else:
            return render_template('err.html')
    return render_template('form.html')

# @app.route("/")
# def BowlingUI():
#     # file containing lists of input scores
#     _filename = 'C:/Users/sayan/PycharmProjects/Bowling/Inputs.txt'
#
#     bowl = BowlingChallenge()
#     giveninputScores = bowl.readInput(_filename)
#     allStrikes = False
#
#     # To change the input list change the keyName on line 23 e.g. 'givenInput' to 'allStrikeInput'
#     inputRolls= giveninputScores['givenInput']
#
#     # inPut = getInput()
#     # inPut1 = literal_eval(getInput())
#     # print(inPut)
#     # print(inPut1)
#     #
#     # print(inputRolls)
#
#
#
#     if((len(inputRolls) <= 21)):
#         finalScore, table = bowl.bowling_score(inputRolls)
#
#         #Set allStrikes flag to True if all elements of input list are 10
#         if all(elem == 10 for elem in inputRolls):
#             allStrikes = True
#
#         # Show output only if 0<=finalScore<=300 and table is not empty and (allStrikes is False or allStrikes is True and number of rolls is 12)
#         if (0 <= finalScore <= 300 and (allStrikes is True and len(inputRolls) == 12) and len(table) != 0) or (0 <= finalScore <= 300 and allStrikes is False and len(table) != 0):
#             return render_template('index.html', title='Bowling Scoreboard', result=table)
#
#         #Error if allStrikes is True and number of inputs > 12
#         elif (len(inputRolls) > 12 and allStrikes is True) or finalScore == 0:
#             return render_template('err.html')
#         else:
#             return render_template('err.html')
#     else:
#         return render_template('err.html')


if __name__ == "__main__":
    app.run()
