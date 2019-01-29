# -*- coding: utf-8 -*-
import unittest
from vm.acceptCoinsState import AcceptCoinsState
from vm.vendingMachine import VendingMachine
from vm.data import vmdata

class AcceptCoinsStateTest(unittest.TestCase):
    
    def setUp(self):
        self.vm = VendingMachine()
        self.acSt = AcceptCoinsState(self.vm)

    def test_insertCoins(self):
        self.acSt.insertCoins(10, 2) 
        self.assertEqual(self.vm.total, 20)
        self.assertEqual(self.vm.coins[10], 2)
        self.acSt.insertCoins(1, 15) 
        self.assertEqual(self.vm.total, 35)
        self.assertEqual(self.vm.coins[10], 2)
        self.assertEqual(self.vm.coins[1],15) 

    def test_choosePrd(self):
        vmdata.coinStore = {10:5, 5:5, 2:0, 1:1}
        vmdata.prdStore = {'A':0, 'B':3, 'C':3, 'D':3}
        self.vm.total = 1
        self.vm.coins = {10:0, 5:0, 2:0, 1:1}
        ret = self.acSt.choosePrd('A')
        self.assertEqual(ret, (False, 'Deal failed, product out of stock, back coins', {1: 1}))
        
        self.vm.total = 1
        self.vm.coins = {10:0, 5:0, 2:0, 1:1}
        ret = self.acSt.choosePrd('B')
        self.assertEqual(ret, (False, 'Deal failed, coins not enough, back coins', {1: 1}))

        self.vm.total = 10
        self.vm.coins = {10:1, 5:0, 2:0, 1:0}
        ret = self.acSt.choosePrd('C')
        self.assertEqual(ret, (False, 'Deal failed, no coins in store, back coins', {10: 1}))

        self.vm.total = 9 
        self.vm.coins = {10:0, 5:1, 2:2, 1:0}
        ret = self.acSt.choosePrd('C')
        self.assertEqual(ret, (True, 'Deal done', {'changes': {1: 1}, 'product': 'C'}))



    def test_getChanges(self):
        vmdata.coinStore = {10:5, 5:5, 2:0, 1:1}
        vmdata.prdStore = {'A':1, 'B':3, 'C':3, 'D':3}

        self.vm.coins = {10:2, 5:1, 2:0, 1:0}
        self.vm.total = 25 
        ret = self.acSt.getChanges("A", 25)
        self.assertTrue(ret[0])
        self.assertEqual(ret[2], {'product': 'A', 'changes': {}})
        self.assertEqual(vmdata.prdStore["A"], 0)
        self.assertEqual(vmdata.coinStore, {10:7, 5:6, 2:0, 1:1})

        self.vm.coins = {10:1, 5:1, 2:0, 1:0}
        self.vm.total = 15 
        ret = self.acSt.getChanges("B", 14)
        self.assertTrue(ret[0])
        self.assertEqual(ret[2],{'product': 'B', 'changes': {1: 1}})
        self.assertEqual(vmdata.prdStore, {'A':0, 'B':2, 'C':3, 'D':3})
        self.assertEqual(vmdata.coinStore, {10:8, 5:7, 2:0, 1:0})

        self.vm.coins = {10:1, 5:1, 2:0, 1:0}
        self.vm.total = 15 
        ret = self.acSt.getChanges("B", 13)
        self.assertFalse(ret[0])

    def test_backCoins(self):
        self.acSt.insertCoins(10, 2) 
        ret = self.acSt.backCoins('xxx')
        self.assertEqual(self.vm.total, 0)
        self.assertEqual(self.vm.coins[10], 0)
        self.assertFalse(ret[0])
        self.assertEqual('Deal failed, xxx, back coins', ret[1])
        self.assertEqual('Deal failed, xxx, back coins', ret[1])
        self.assertEqual({10:2}, ret[2])
