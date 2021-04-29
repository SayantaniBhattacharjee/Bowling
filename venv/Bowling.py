from ast import literal_eval

class BowlingChallenge:
    
    _table_data = []

    ############################### Convert all inputs to Integer #################################
    def convertStringstoInt(self, val):
        val = val.replace('[', '').replace(']', '')
        inPutList = list(val.split(","))
        for i in range(0, len(inPutList)):
            try:
                inPutList[i] = int(inPutList[i])
            except ValueError:
                if (inPutList[i] == ' /' or inPutList[i] == '/' or inPutList[i] == '/ '):
                    inPutList[i] = 10 - int(inPutList[i - 1])
                elif (inPutList[i] == ' X' or inPutList[i] == 'X' or inPutList[i] == 'X '):
                    inPutList[i] = 10
                elif (inPutList[i] == ' -' or inPutList[i] == '-' or inPutList[i] == '- '):
                    inPutList[i] = 0
        return inPutList
    
    ############################### Read inputs from Inputs.txt #########################
    def readInput(self, file):
        inputScores = {}
        try:
            fp = open(file)
            content = fp.readlines()
        finally:
            fp.close()
        content = [x.strip() for x in content]
        for input in content:
            #storing the input scores as dict(key, val)
            (key, val) = input.split('=')
            key = key[:-1]
            val = val[1:]

            inputScores[key] = self.convertStringstoInt(val)

        return inputScores

    ################# Store each frame rolls and cumulative scores in a dictionary #################
    def eachFrameRolls(self, data_i, frameID, roll1, roll2, roll3, frameScore):
        data_i['frame'] = frameID
        data_i['roll1'] = roll1
        data_i['roll2'] = roll2
        data_i['roll3'] = roll3
        data_i['total'] = frameScore
        return data_i

    ###################################### Score Calculator ########################################
    def bowling_score(self, rolls):
        self._table_data.clear()
        frameScore = 0
        totalScore = 0
        frameID = 0
        excessScore = 0
        nextframe = True
        data_i={}
        try:
            for roll_index, roll in enumerate(rolls):
                if(frameID == 10):
                    break
                if(roll == 10):
                    frameScore += rolls[roll_index + 1]
                    frameScore += rolls[roll_index + 2]
                    if(frameID != 9):
                        self.eachFrameRolls(data_i, frameID + 1, roll, None, None, frameScore)
                        self._table_data.append(data_i)
                    elif (frameID == 9):
                        self.eachFrameRolls(data_i, frameID + 1, roll, rolls[roll_index + 1], rolls[roll_index + 2], frameScore)
                    frameID += 1
                elif not nextframe:
                    if rolls[roll_index - 1] + roll == 10:
                        frameScore += rolls[roll_index + 1]
                        self.eachFrameRolls(data_i, frameID + 1,  rolls[roll_index - 1], roll, None, frameScore)
                    frameID += 1
                    nextframe = True
                else:
                    nextframe = False
                    data_i = {}
                    self.eachFrameRolls(data_i, frameID + 1, roll, rolls[roll_index + 1], None, frameScore)
                    self._table_data.append(data_i)
                frameScore += roll

                data_i={}
                if(frameID == 10):
                    if(roll == 10):
                        self.eachFrameRolls(data_i, frameID, roll, rolls[roll_index + 1], rolls[roll_index + 2], frameScore)
                    elif(rolls[roll_index - 1] + roll == 10):
                        self._table_data.pop()
                        self.eachFrameRolls(data_i, frameID,  rolls[roll_index - 1], roll, rolls[roll_index + 1], frameScore)
                    elif(roll_index + 1 != len(rolls)):
                        #self._table_data.pop()
                        self.eachFrameRolls(data_i, frameID + 1, roll, rolls[roll_index + 1], None,
                                            frameScore)
                    elif (roll != 10 and roll_index + 1 == len(rolls)):
                        self._table_data.pop()
                        self.eachFrameRolls(data_i, frameID, rolls[roll_index - 1], roll, None,
                                        frameScore)
            self._table_data.append(data_i)

            #Brute Force approach towards error handling inputs with frames > 10
            for i in self._table_data:
                if i['frame'] > 10:
                    excessScore = i['roll1'] + i['roll2']
                    self._table_data = []

            totalScore = frameScore - excessScore
            return totalScore, self._table_data

        except IndexError:
            self._table_data = []
            print('Looks like the game still has a few rolls left!')
            return totalScore, self._table_data

if __name__ == '__main__':
    
    file = '../Inputs.txt' 
    game = BowlingChallenge()
    
    giveninputScores = game.readInput(file)
    inputRolls = giveninputScores['givenStringsInput']


    print(game.bowling_score(inputRolls))