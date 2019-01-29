# -*- coding: utf-8 -*-

from state import State
from data import vmdata 
import math

class AcceptCoinsState(State):
    """ The State of the vending machine after accepting coins """

    def __init__(self, vendingMachine):
        """Init the class with a vendingMachine instance"""
        self.vm = vendingMachine
    
    def choosePrd(self, prd):
        """This method trigger the deal 
        Args:
            prd: string, should be in the product list
        Returns:
            tuple: (bool, string, dict)
        """
        if vmdata.getPrdStore(prd) == 0:
            return self.backCoins('product out of stock')
        prdPrice = vmdata.getPrdPrice(prd)
        if self.vm.total < prdPrice:
            return self.backCoins('coins not enough')
        ret = self.getChanges(prd, prdPrice)
        if not ret[0]:
            return self.backCoins(ret[1])
        self.vm.__init__()
        return ret


    def getChanges(self, prd, prdPrice):    
        """This method get the changes and update db store (vmdata)
        Args:
            prd: string, must in the product list
            prdPrice, int
        Returns:
            tuple: (bool, string, dict)
        """
        avlCoins, outputCoins = {}, {} 
        coinTypes = sorted(self.vm.coins, reverse=True)
        for coin in coinTypes:
            avlCoins[coin] = vmdata.coinStore[coin] + self.vm.coins[coin] 
        changes = self.vm.total - prdPrice
        for value in coinTypes:
            if changes == 0:
                break
            cnt = min(int(math.floor(changes/value)), avlCoins[value])
            if cnt > 0:
                outputCoins[value] = cnt
                changes -= value * cnt
        if changes != 0:
            return False, 'no coins in store', {}
        for k in avlCoins:
            if k not in outputCoins:
                vmdata.coinStore[k] = avlCoins[k]
            else:
                vmdata.coinStore[k] = avlCoins[k] - outputCoins[k]
        vmdata.subPrdStore(prd, 1)
        return True, 'Deal done', {'product':prd, 'changes':outputCoins} 

        
        
    def insertCoins(self, coin, num):
        self.vm.coins[coin] += num
        self.vm.total += coin * num
        return True, 'accepted coins', {'total':self.vm.total, 'coins':self.vm.coins}
        
    def backCoins(self, msg = 'apply back coins'):
        if self.vm.total > 0:
            changes = {}
            for k in self.vm.coins:
                if self.vm.coins[k] > 0:
                    changes[k] = self.vm.coins[k]
            self.vm.__init__()
            return False, 'Deal failed, ' + msg + ', back coins', changes 
        return False, "No coins return.",{}
        
