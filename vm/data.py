# -*- coding: utf-8 -*-
class Data(object):
    """
    A Singleton class storing and manipulating data.
    """
    def __init__(self):
        self.prdPrice = {"A": 25, "B": 13, "C": 8, "D": 12}
        self.prdStore = {"A": 1, "B": 3, "C": 3, "D": 3}
        self.coinStore = {10: 5, 5: 5, 2: 5, 1: 5}
    
    def getPrdPrice(self, item):
        return self.prdPrice[item]

    def getPrdStore(self, item):
        return self.prdStore[item]

    def getCoinStore(self, coin):
        return self.coinStore[coin]

    def addPrdStore(self, product, num):
        self.prdStore[product] += num
        return True,self.prdStore

    def addCoinStore(self, coin, num):
        self.coinStore[coin] += num
        return True,self.coinStore
        
    def subPrdStore(self, item, num = 1):
        if self.prdStore[item] < num:
            return False, self.prdStore
        self.prdStore[item] -= num
        return True,self.prdStore

    def subCoinStore(self, coin, num):
        if self.coinStore[coin] < num:
            return False, self.coinStore
        self.coinStore[coin] -= num
        return True, self.coinStore


vmdata = Data()
