import unittest
from montyHall import choose, isWinner, openDoor, switch, doors

class MontyHallTest(unittest.TestCase):

    def testChooseDoor(self):
        choose()
        self.assertTrue(doors['chosen'] <= 3)
        self.assertTrue(doors['chosen'] > 0)
        
    def testWin(self):
        doors['chosen'] = 1
        self.assertTrue(isWinner())

    def testLose(self):
        doors['chosen'] = 2
        self.assertFalse(isWinner())

    def testPeekWithWrongChoice(self):
        doors['chosen'] = 2
        openDoor()
        self.assertEquals(doors['open'], 3)
        doors['chosen'] = 3
        openDoor()
        self.assertEquals(doors['open'], 2)

    def testPeekWithRightChoice(self):
        doors['chosen'] = 1
        openDoor()
        self.assertIn(doors['open'], [2,3])

    def testRandomPeek(self):
        choose()
        openDoor()
        self.assertNotEquals(doors['open'], doors['chosen'])
        self.assertNotEquals(doors['open'], doors['prize'])

    def testSwitch(self):
        doors['chosen'] = 1
        doors['open'] = 2
        switch()
        self.assertEquals(doors['chosen'], 3)
        switch()
        self.assertEquals(doors['chosen'], 1)


if __name__ == '__main__':
    unittest.main()
