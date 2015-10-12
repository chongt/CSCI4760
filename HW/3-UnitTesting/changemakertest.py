#
# Test code for the ChangeMaker class, which computes change from
# a purchase as a list [quarters, dimes, nickels, pennies]
#

import unittest
import changemaker

class TestChangeMaker(unittest.TestCase):

    def test_coinlist(self):
        '''Test coinlist method, which 
        converts an integer number of cents into a list of coins
        `'''
        changer = changemaker.ChangeMaker()
        self.assertEqual(changer.coinlist(87),  [3,1,0,2])
        self.assertEqual(changer.coinlist(50),  [2,0,0,0])
        self.assertEqual(changer.coinlist(0),   [0,0,0,0])
        self.assertEqual(changer.coinlist(223), [8,2,0,3])

    def test_changelist(self):
        '''Test 'changelist' method, which 
        computes the change from a purchase as a list of coins
        `'''
        changer = changemaker.ChangeMaker()
        self.assertEqual(changer.changelist(13,100),[3,1,0,2])
        self.assertEqual(changer.changelist(53,100),[1,2,0,2])
        self.assertEqual(changer.changelist(100,100),[0,0,0,0])
        self.assertEqual(changer.changelist(45,100),[2,0,1,0])

if __name__ == '__main__':
    unittest.main()
