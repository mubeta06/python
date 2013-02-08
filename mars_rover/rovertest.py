#!/usr/bin/env python
"""This file is part of a solution to the Mars Rover Exercise.

Matthew Baker <mu.beta.06@gmail.com> 2013

Unit test for rover module.

Since the Rover object is merely a container for it's current position and 
heading we can only test the getters and setters.
"""

import math
import unittest

import rover


class TestRover(unittest.TestCase):

    position = (2, 2, 0)
    heading = (0, 90)

    def setUp(self):
        pass

    def tearDown(self): 
        pass

    def test_creation(self):
        """Test creation of Rover container.
        """
        r = rover.Rover(self.position, self.heading)
        self.assert_(r.position == self.position)
        self.assert_(r.heading == self.heading)

    def test_angle_limits(self):
        """Test both Azimuth and Zenith angle limits.
        """
        r = rover.Rover(self.position, self.heading)
        def set_angle(angle):
            r.heading = angle
        self.assertRaises(Exception, set_angle, (-5, 10))
        self.assertRaises(Exception, set_angle, (5, -10))
        self.assertRaises(Exception, set_angle, (375, 10))
        self.assertRaises(Exception, set_angle, (75, 1110))
        set_angle((0, 2*math.pi))
        self.assert_(r.heading == (0, 2*math.pi))


if __name__ == '__main__':
    unittest.main()
