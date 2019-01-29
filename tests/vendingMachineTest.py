# -*- coding: utf-8 -*-
import unittest
from vm.data import vmdata 
from vm.initState import InitState
from vm.acceptCoinsState import AcceptCoinsState
from vm.vendingMachine import VendingMachine 

class VendingMachineTest(unittest.TestCase):

    def setUp(self):
        self.vm = VendingMachine()

    def test_choosePrd(self):
        ret = self.vm.choosePrd('J')
        self.assertFalse(ret[0])
        self.assertEqual(ret[1],'Product out of range')

    def test_insertCoins(self):
        ret = self.vm.insertCoins(11, 2)
        self.assertEqual(ret[1], 'Coin out of range')
        ret = self.vm.insertCoins(10, 2.5)
        self.assertEqual(ret[1], 'Coin out of range')
        ret = self.vm.insertCoins(10, -1)
        self.assertEqual(ret[1], 'Coin out of range')

