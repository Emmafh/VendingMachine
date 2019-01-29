# -*- coding: utf-8 -*-

from data import vmdata 
from initState import InitState
from acceptCoinsState import AcceptCoinsState
import logging

class VendingMachine(object):

    def __init__(self):
        """
        Init VendingMachine with the following data
            initSt: the init state of vending machine
            acSt: the state after accepting coins
            current: initiate the current state as initSt
            coins: initiate the acceptted coins
            total: initiate the acceptted total money
        """
        self.initSt = InitState(self)   #The init state of vending machine
        self.acSt = AcceptCoinsState(self)  #the state of accepting coins vending machine
        self.current = self.initSt  #set current state as init state
        self.coins = {10: 0, 5: 0, 2: 0, 1: 0}  #the coins the vending machine can accept in one transaction
        self.total = 0 #total money

    def choosePrd(self, prd):
        """This method trigger the deal after inserting coins 
        Args:
            prd: string, should be in the product list
        Returns:
            tuple: (bool, string, dict)
        """
        if prd not in vmdata.prdStore:
            return False, "Product out of range", {}
        try:
            ret = self.current.choosePrd(prd)
            return ret
        except:
            logging.error("Choose product %s error"%(prd))
            self.backCoins()

    def insertCoins(self, coin, num):
        """Insert coins during one transaction 
        Args:
            coin: int, must in the coins range
            num: int, > 0
        Returns:
            tuple: (bool, string, dict)
        """
        if coin not in self.coins or not isinstance(num, int) or num < 1:
            return False, 'Coin out of range', {}
        try:
            return self.current.insertCoins(coin, num)
        except:
            logging.error("Insert coins %d, %d error"%(coin, num))
            self.backCoins()

    def backCoins(self):
        """Return coins and reset the status of the vending machine 
        Returns:
            tuple: (bool, string, dict)
        """
        return self.current.backCoins()

    def adminAddPrdStore(self, prd, num):
        """Used by admin users to add products
        Args:
            prd: string, must in the product range
            num: int, > 0
        Returns:
            tuple: (bool, string, dict)
        """
        if not self.__checkProduct(prd, num):
            return False, "parameter error", {}
        try:
            ret = vmdata.addPrdStore(prd, num) 
            return True, "Add success, current product store", ret[1]
        except:
            logging.error("Add product error")
        
    def adminAddCoinStore(self, coin, num):
        """Used by admin users to add coins
        Args:
            coin: int, must in the coins range
            num: int, > 0
        Returns:
            tuple: (bool, string, dict)
        """
        if not self.__checkCoin(coin, num):
            return False, "parameter error", {}
        try:
            ret = vmdata.addCoinStore(coin, num) 
            return True, "Add success, current product store", ret[1]
        except:
            logging.error("Add coin error")
            

    def adminSubPrdStore(self, prd, num):
        """Used by admin users to reduce products
        Args:
            prd: string, must in the product range
            num: int, > 0
        Returns:
            tuple: (bool, string, dict)
        """
        if not self.__checkProduct(prd, num):
            return False, "parameter error", {}
        try:
            ret = vmdata.subPrdStore(prd, num)
            if not ret[0]:
                return False, "sub error", ret[1]
            return True, "Sub success", ret[1]
        except:
            logging.error("Sub product error")

    def adminSubCoinStore(self, coin, num):
        """Used by admin users to reduce coins
        Args:
            coin: int, must in the coins range
            num: int, > 0
        Returns:
            tuple: (bool, string, dict)
        """
        if not self.__checkCoin(coin, num):
            return False, "parameter error", {}
        try:
            ret = vmdata.subCoinStore(coin, num)
            if not ret[0]:
                return False, "sub error", ret[1]
            return True, "Sub success", ret[1]
        except:
            logging.error("Sub coin error")

    def __checkProduct(self, prd, num):
        """Check product parameters range"""
        if prd not in vmdata.prdStore or not isinstance(num, int) or num < 1:
            return False         
        return True

    def __checkCoin(self, coin, num):
        """Check coin parameters range"""
        if coin not in vmdata.coinStore or not isinstance(num, int) or num < 1:
            return False
        return True


