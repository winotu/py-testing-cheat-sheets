#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 KZ
#
# Distributed under terms of the MIT license.

import animal
import mock

def mocked_speak():
    print r"""
o'')}____//
 `_/      )
 (_(_/-(_/
    """
    print "Hau"

def test():
    """ test """
    my_cat = animal.Cat('Pusheen') # Cat with name Pusheen
    my_cat.speak()              # [(datatime)] Miauu, my name is Pusheen"

    # fake a Cat
    mock_cat = mock.Mock(spec=animal.Cat, name="Fake Cat")
    mock_cat.speak = mocked_speak # mock_cat.speak is auto Mock() object

    print "Is mock_cat a Cat?"
    print isinstance(mock_cat, animal.Cat)
    mock_cat.speak()

if __name__ == "__main__":
    test()
