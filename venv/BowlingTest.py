import unittest
from Bowling import BowlingChallenge


class MyTestCase(unittest.TestCase):

    _filename = 'C:/Users/sayan/PycharmProjects/Bowling/Inputs.txt'
    
    def setUp(self):
        self.bowl = BowlingChallenge()
        self.giveninputScores = self.bowl.readInput(self._filename)

    def test_givenInput(self):
        inputRolls = self.giveninputScores['givenInput']
        finalScore = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 167)
        
    def test_spareInTenth(self):
        inputRolls = self.giveninputScores['spareInTenthInput']
        finalScore = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 153)
        
    def test_noStrikeOrSpareTenth(self):
        inputRolls = self.giveninputScores['noSpareOrStrikeinTenthInput']
        finalScore = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 139)
    
    def test_allStrike(self):
        inputRolls = self.giveninputScores['allStrikeInput']
        finalScore = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 300)

    def test_singleStrike(self):
        inputRolls = self.giveninputScores['singleStrikeInput']
        finalScore = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 29)
    
    


if __name__ == '__main__':
    unittest.main()
