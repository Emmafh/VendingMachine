# -*- coding: utf-8 -*-
import unittest
from vm.data import vmdata

class DataTest(unittest.TestCase):

    def test_getPrdPrice(self):
        self.assertEqual(vmdata.prdPrice['A'], vmdata.getPrdPrice('A'))

    def test_getPrdStore(self):
        self.assertEqual(vmdata.prdStore['A'], vmdata.getPrdStore('A'))

    def test_getCoinStore(self):
        self.assertEqual(vmdata.coinStore[5], vmdata.getCoinStore(5))

    def test_addPrdStore(self):
        vmdata.prdStore = {"A": 1, "B": 3, "C": 3, "D": 3}
        ret = vmdata.addPrdStore('B', 2)
        self.assertEqual(ret[1], {"A": 1, "B": 5, "C": 3, "D": 3})

    def test_addCoinStore(self):
        vmdata.coinStore = {10: 5, 5: 5, 2: 5, 1: 5} 
        ret = vmdata.addCoinStore(2, 2)
        self.assertEqual(ret[1], {10: 5, 5: 5, 2: 7, 1: 5})

    def test_subPrdStore(self):
        vmdata.prdStore = {"A": 1, "B": 3, "C": 3, "D": 3}
        ret = vmdata.subPrdStore('B', 3)
        self.assertEqual(ret[1], {"A": 1, "B": 0, "C": 3, "D": 3})
        ret = vmdata.subPrdStore('B', 1)
        self.assertFalse(ret[0])
        
    def test_subCoinStore(self):
        vmdata.coinStore = {10: 5, 5: 5, 2: 5, 1: 5} 
        ret = vmdata.subCoinStore(10, 5)
        self.assertEqual(ret[1], {10: 0, 5: 5, 2: 5, 1: 5})
        ret = vmdata.subCoinStore(10, 1)
        self.assertFalse(ret[0])
