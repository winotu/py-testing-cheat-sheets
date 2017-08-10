#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 KZ
#
# Distributed under terms of the MIT license.

import animal
import mock

def test():
    """ test """
    my_cat = animal.Cat('Pusheen') # Cat with name Pusheen
    my_cat.speak()              # [(datatime)] Miauu, my name is Pusheen"

    # fake a Cat
    mock_cat = mock.Mock(name="Fake Cat")
    def hau():
        print "Hau"
    mock_cat.speak.side_effect = [hau()] # mock_cat.speak is auto Mock() object
    mock_cat.speak()

if __name__ == "__main__":
    test()
