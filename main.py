#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vm.vendingMachine import VendingMachine

def main():
    vm = VendingMachine()

    """first deal, expect success"""
    print "------------First deal------------"
    print vm.insertCoins(10, 2)
    print vm.insertCoins(5, 1)
    print vm.insertCoins(1, 2)
    print vm.choosePrd('A')

    """second deal, expect out of stock"""
    print "------------Second deal------------"
    print vm.insertCoins(10, 1)
    print vm.insertCoins(5, 4)
    print vm.insertCoins(1, 2)
    print vm.choosePrd('A')

    """third deal, expect back coins"""
    print "------------Third deal------------"
    print vm.insertCoins(2, 1)
    print vm.insertCoins(5, 2)
    print vm.insertCoins(1, 1)
    print vm.backCoins()

    """admin add product store"""
    print "------------Admin add product------------"
    print vm.adminAddPrdStore('A', 2)

    """fourth deal, expect success"""
    print "------------Fourth deal------------"
    print vm.insertCoins(10, 2)
    print vm.insertCoins(5, 1)
    print vm.insertCoins(1, 2)
    print vm.choosePrd('A')

    """admin reduce coins store, expect False"""
    print "------------Admin reduce coins------------"
    print vm.adminSubCoinStore(2, 10)

    """admin reduce coins store, expect True"""
    print "------------Admin reduce coins------------"
    print vm.adminSubCoinStore(2, 3)

    """admin reduce coins store, expect True"""
    print "------------Admin reduce coins------------"
    print vm.adminSubCoinStore(1, 9)

    """fifth deal, expect fail"""
    print "------------Fifth deal------------"
    print vm.insertCoins(10, 1)
    print vm.insertCoins(5, 1)
    print vm.choosePrd('B')

    """admin add coins store, expect True"""
    print "------------Admin add coins------------"
    print vm.adminAddCoinStore(1, 5)
    print vm.adminAddCoinStore(2, 5)

    """sixth deal, expect success"""
    print "------------Sixth deal------------"
    print vm.insertCoins(10, 1)
    print vm.insertCoins(5, 1)
    print vm.choosePrd('B')

if __name__ == '__main__':
    main()
