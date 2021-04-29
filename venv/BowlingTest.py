import unittest
from Bowling import BowlingChallenge


class MyTestCase(unittest.TestCase):

    _filename = '../Inputs.txt'
    
    def setUp(self):
        self.bowl = BowlingChallenge()
        self.giveninputScores = self.bowl.readInput(self._filename)

    def test_givenInput(self):
        inputRolls = self.giveninputScores['givenInput']
        finalScore, total = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 167)
        
    def test_givenInputWithStrings(self):
        inputRolls = self.giveninputScores['givenStringsInput']
        finalScore, total = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 167)
        
    def test_spareInTenth(self):
        inputRolls = self.giveninputScores['spareInTenthInput']
        finalScore, total = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 153)
        
    def test_noStrikeOrSpareTenth(self):
        inputRolls = self.giveninputScores['noSpareOrStrikeinTenthInput']
        finalScore, total = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 139)
    
    def test_allStrike(self):
        inputRolls = self.giveninputScores['allStrikeInput']
        finalScore, total = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 300)

    def test_singleStrike(self):
        inputRolls = self.giveninputScores['singleStrikeInput']
        finalScore, total = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 29)
    
    def test_randomInput(self):
        inputRolls = self.giveninputScores['randomInput']
        finalScore, total = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 122)

    def test_randomInputWithSpare(self):
        inputRolls = self.giveninputScores['randomInputWithSpareTenth']
        finalScore, total = self.bowl.bowling_score(inputRolls)
        self.assertEqual(finalScore, 133)


if __name__ == '__main__':
    unittest.main()
