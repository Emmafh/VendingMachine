#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from vm.initState import InitState
from vm.vendingMachine import VendingMachine

class InitStateTest(unittest.TestCase):
    
    def setUp(self):
        self.vm = VendingMachine()
        self.initSt = InitState(self.vm)

    def test_choosePrd(self):
        ret = self.initSt.choosePrd('A')
        self.assertFalse(ret[0])
        self.assertEqual('Please insert coins at first.', ret[1])

    def test_backCoins(self):
        ret = self.initSt.backCoins()
        self.assertFalse(ret[0])
        self.assertEqual('No coins return.', ret[1])

