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


    def test_add_rover(self):
        """Test adding Rover."""
        rc = rovercontroller.RoverController(((0, 0, 0), (5, 5, 5)))
        rc.add_rover('r0', (1, 2, 3), (0, 0))

        #test successful add
        self.assertTrue('r0' in rc.rovers.keys())

        # add Rover with same id
        self.assertRaises(Exception, rc.add_rover, 'r0', (2, 5, 3), (0, 0))

        #add Rover in preoccupied position
        self.assertRaises(Exception, rc.add_rover, 'r1', (1, 2, 3), (0, 0))

        #add Rover(s) out of grid
        self.assertRaises(Exception, rc.add_rover, 'r1', (-1, 2, 3), (0, 0))
        self.assertRaises(Exception, rc.add_rover, 'r1', (6, 5, 5), (0, 0))
        self.assertRaises(Exception, rc.add_rover, 'r1', (5, -1, 5), (0, 0))
        self.assertRaises(Exception, rc.add_rover, 'r1', (5, 6, 5), (0, 0))
        self.assertRaises(Exception, rc.add_rover, 'r1', (5, 1, 10), (0, 0))
        self.assertRaises(Exception, rc.add_rover, 'r1', (5, 1, -10), (0, 0))

        #test other quadrants...
        rc = rovercontroller.RoverController(((0, 0, 0), (-5, 5, -5)))
        #rc.add_rover('r0', (1, 2, 3), (0, 0))

    def test_get_rover(self):
        """"Test getting a Rover."""
        rc = rovercontroller.RoverController(((0, 0, 0), (5, 5, 5)))
        rc.add_rover('r0', (1, 2, 3), (0, 0))
        self.assertEquals(rc.get_rover('r0'), rc.rovers['r0'])
        self.assertRaises(Exception, rc.get_rover, 'r1')

    def test_is_empty(self):
        """Test if position is empty."""
        rc = rovercontroller.RoverController(((0, 0, 0), (5, 5, 5)))
        rc.add_rover('r0', (1, 2, 3), (0, 0))
        [self.assertFalse(rc.is_empty((x, y, z))) if (x, y, z) == (1, 2, 3) 
                else self.assertTrue(rc.is_empty((x, y, z)))
                for z in range(6) for y in range(6) for x in range(6)]

    def test_in_grid(self):
        """Test if position is in grid."""
        rc = rovercontroller.RoverController(((0, 0, 0), (-5, 5, 0)))
        self.assertTrue(rc.in_grid((0, 0, 0)))
        self.assertFalse(rc.in_grid((0, 0, 1)))
        self.assertFalse(rc.in_grid((0, 0, -1)))
        self.assertTrue(rc.in_grid((-5, 5, 0)))
        self.assertFalse(rc.in_grid((-6, 5, 0)))
        self.assertFalse(rc.in_grid((-5, 6, 0)))
        self.assertFalse(rc.in_grid((-5, -1, 0)))


if __name__ == '__main__':
    unittest.main()
