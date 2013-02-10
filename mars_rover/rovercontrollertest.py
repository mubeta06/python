#!/usr/bin/env python
"""This file is part of a solution to the Mars Rover Exercise.

Matthew Baker <mu.beta.06@gmail.com> 2013

Unit test for rovercontroller module.

I have largely omitted tests for type safeness as porting this implementation to 
a type safe language will take care of this.
"""

import math
import unittest

import rovercontroller


class TestRoverController(unittest.TestCase):

    origin = (0, 0, 0)
    vertex = (5, 5)
    heading = (math.pi/2, math.pi/2)
    #r0 = rover.Rover(position, heading)
    #r1 = rover.Rover(position, heading)

    def setUp(self):
        pass

    def tearDown(self): 
        pass

    def test_creation(self):
        """Test creation of Rover container."""
        pass


if __name__ == '__main__':
    unittest.main()
