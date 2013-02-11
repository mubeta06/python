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

    def test_creation(self):
        """Test creation of Rover container."""
        r = rover.Rover(self.position, self.heading)
        self.assertEqual(r.position, self.position)
        self.assertEqual(r.heading, self.heading)

    def test_angle_limits(self):
        """Test both Azimuth and Zenith angle are mod 2pi."""
        self.r.heading = (2*math.pi, 2*math.pi/2)        
        self.assertGreater(self.r.heading, 2*math.pi)
        self.r.heading = (3*math.pi, 3*math.pi/2)
        self.assertGreater(self.r.heading, 2*math.pi)
        self.r.heading = (-2*math.pi, -2*math.pi)
        self.assertGreater(self.r.heading, 2*math.pi)
        self.r.heading = (0, 0)        
        self.assertGreater(self.r.heading, 2*math.pi)

    def test_set_position(self):
        """Test position setter."""
        def set_position(position):
            self.r.position = position
        self.assertRaises(ValueError, set_position, (0, 2))
        self.assertRaises(ValueError, set_position, (0))
        self.assertRaises(ValueError, set_position, 0)


if __name__ == '__main__':
    unittest.main()
