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
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \\ )-`( , o o)
           `-    \`_`"'-
"""

    def speak(self):
        """ Speech method"""
        self._icon()
        print "[{}] Miauu, my name is {}".format(datetime.datetime.now(), self.name)
