# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class State(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def choosePrd(self):
        pass

    @abstractmethod
    def insertCoins(self):
        pass

    @abstractmethod
    def backCoins(self):
        pass



