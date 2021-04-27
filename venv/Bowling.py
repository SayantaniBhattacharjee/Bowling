from ast import literal_eval

class BowlingChallenge:
    
    def readInput(self, file):
        inputScores = {}
        try:
            fp = open(file)
            content = fp.readlines()
        finally:
            fp.close()
        content = [x.strip() for x in content]
        for input in content:
            (key, val) = input.split('=')
            key = key[:-1]
            val = val[1:]
            inputScores[key] = literal_eval(val)
        return inputScores

    def bowling_score(self, rolls):

        frameScore = 0
        totalScore = 0
        frameID = 0
        nextframe = True
        for roll_index, roll in enumerate(rolls):
            if frameID == 10:
                break
            if roll == 10:
                frameScore += rolls[roll_index + 1]
                frameScore += rolls[roll_index + 2]
                frameID += 1
            elif not nextframe:
                if rolls[roll_index - 1] + roll == 10:
                    frameScore += rolls[roll_index + 1]
                frameID += 1
                nextframe = True
            else:
                nextframe = False
            frameScore += roll
            #print(roll_index, ' ', roll)
            #print(frameScore)
            #print('\n')
        totalScore = frameScore

        return totalScore

if __name__ == '__main__':
    file = 'C:/Users/sayan/PycharmProjects/Bowling/Inputs.txt'
    
    game = BowlingChallenge()
    
    giveninputScores = game.readInput(file)
    inputRolls = giveninputScores['givenInput']
    print(game.bowling_score(inputRolls))