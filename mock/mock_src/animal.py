#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 KZ
#
# Distributed under terms of the MIT license.

""" base Cat module """
import datetime

class Cat(object):
    """ Cat object """

    def __init__(self, name):
        """ object init """
        self.name = name

    @staticmethod
    def _icon():
        print r"""
           A___A
     ____ / o o \
   /~____   ='= /
  (______)__m_m_)
"""

    def speak(self):
        """ Speech method"""
        self._icon()
        print "[{}] Miauu, my name is {}".format(datetime.datetime.now(), self.name)
