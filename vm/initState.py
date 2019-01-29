# -*- coding: utf-8 -*-

from state import State
from acceptCoinsState import AcceptCoinsState

class InitState(State):

    def __init__(self, vendingMachine):
        self.vm = vendingMachine
        
    def choosePrd(self, prd):
        """In init state, user should insert coins at first 
        Args:
            prd: string, should be in the product list
        Returns:
            tuple: (bool, string, dict)
        """
        return False, "Please insert coins at first.", {} 
        
    def insertCoins(self, coin, num):
        """this method will turn the state to acceptCoinsState. 
        Args:
            coin: int, should be in the product list
            num: int, shoule be larger than 0
        Returns:
            tuple: (bool, string, dict)
        """
        self.vm.current = self.vm.acSt
        return self.vm.insertCoins(coin, num)
        
    def backCoins(self):
        """In init state, there is no coin to return. 
        Returns:
            tuple: (bool, string, dict)
        """
        return False, "No coins return.", {}

