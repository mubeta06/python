#!/usr/bin/env python
"""This file is part of a solution to the Mars Rover Exercise.

Matthew Baker <mu.beta.06@gmail.com> 2013

Unit test for rover module.

Since the Rover object is merely a container for it's current position and 
heading we should test the getters and setters.

I have largely omitted tests for type safeness as porting this implementation to 
a type safe language will take care of this.
"""

import math
import unittest

import rover


class TestRover(unittest.TestCase):

    position = (2, 2, 0)
    heading = (math.pi/2, math.pi/2)
    r = rover.Rover(position, heading)

    def setUp(self):
        pass

    def tearDown(self): 
        pass

    def test_creation(self):
        """Test creation of Rover container."""
        r = rover.Rover(self.position, self.heading)
        self.assert_(r.position == self.position)
        self.assert_(r.heading == self.heading)

    def test_angle_limits(self):
        """Test both Azimuth and Zenith angle are mod 2pi."""
        self.assert_(self.r.heading > 2*math.pi)

    def test_set_position(self):
        """Test position setter."""
        def set_position((x, y, z)):
            self.r.position = (x, y, z)
        self.assertRaises(Exception, set_position, (0, 2))
        self.assertRaises(Exception, set_position, (0))
        self.assertRaises(Exception, set_position, 0)


if __name__ == '__main__':
    unittest.main()
