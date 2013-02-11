#!/usr/bin/env python
"""This file is part of a solution to the Mars Rover Exercise.

Matthew Baker <mu.beta.06@gmail.com> 2013

Unit test for marsrovercontroller module.

I have largely omitted tests for type safeness as porting this implementation to 
a type safe language will take care of this.
"""

import math
import unittest

import marsrovercontroller


class TestMarsRoverController(unittest.TestCase):


    def test_move_first_quadrant(self):
        """Test MarsRoverController move method in first quadrant."""
        mrc = marsrovercontroller.MarsRoverController(((0, 0, 0), (5, 5, 0)))
        mrc.add_rover('r0', (2, 1, 0), (math.pi/2, math.pi/2))
        mrc.move('r0', 1)
        self.assertEquals(mrc.get_rover('r0').position, (2, 2, 0))
        mrc.move('r0', 3)
        self.assertEquals(mrc.get_rover('r0').position, (2, 5, 0))
        self.assertRaises(Exception, mrc.move, 'r0', 1)

    def test_move_second_quadrant(self):
        """Test MarsRoverController move method in second quadrant."""
        mrc = marsrovercontroller.MarsRoverController(((0, 0, 0), (-5, 5, 0)))
        mrc.add_rover('r0', (-1, 2, 0), (math.pi, math.pi/2))
        mrc.move('r0', 4)
        self.assertEquals(mrc.get_rover('r0').position, (-5, 2, 0))
        mrc.turn('r0', math.pi/2, 0)
        mrc.move('r0', 1)
        self.assertEquals(mrc.get_rover('r0').position, (-5, 1, 0))
        mrc.turn('r0', math.pi/2, 0)
        mrc.turn('r0', math.pi/2, 0)
        mrc.move('r0', 1)
        self.assertEquals(mrc.get_rover('r0').position, (-5, 2, 0))

    def test_move_third_quadrant(self):
        """Test MarsRoverController move method in third quadrant."""
        mrc = marsrovercontroller.MarsRoverController(((0, 0, 0), (-5, -5, 0)))
        mrc.add_rover('r0', (-1, -1, 0), (3*math.pi/2, math.pi/2))
        mrc.move('r0', 4)
        self.assertEquals(mrc.get_rover('r0').position, (-1, -5, 0))
        mrc.turn('r0', -math.pi/2, 0)
        mrc.move('r0', 1)
        self.assertEquals(mrc.get_rover('r0').position, (-2, -5, 0))
        mrc.turn('r0', -math.pi/2, 0)
        mrc.move('r0', 1)
        self.assertEquals(mrc.get_rover('r0').position, (-2, -4, 0))

    def test_move_foruth_quadrant(self):
        """Test MarsRoverController move method in fourth quadrant."""
        mrc = marsrovercontroller.MarsRoverController(((0, 0, 0), (5, -5, 0)))
        mrc.add_rover('r0', (1, -1, 0), (0, math.pi/2))
        mrc.move('r0', 1)
        self.assertEquals(mrc.get_rover('r0').position, (2, -1, 0))
        mrc.turn('r0', -math.pi/2, 0)
        mrc.move('r0', 1)
        self.assertEquals(mrc.get_rover('r0').position, (2, -2, 0))
        mrc.turn('r0', -math.pi/2, 0)
        mrc.move('r0', 1)
        self.assertEquals(mrc.get_rover('r0').position, (1, -2, 0))

    def test_move_backwards(self):
        """Test Rover has no reverse."""
        mrc = marsrovercontroller.MarsRoverController(((0, 0, 0), (5, 5, 0)))
        mrc.add_rover('r0', (2, 1, 0), (math.pi/2, math.pi/2))
        self.assertRaises(Exception, mrc.move, 'r0', -1)

    def test_move_float(self):
        """Test Rover can only be moved integer grid positions."""
        mrc = marsrovercontroller.MarsRoverController(((0, 0, 0), (5, 5, 0)))
        mrc.add_rover('r0', (2, 1, 0), (math.pi/2, math.pi/2))
        self.assertRaises(Exception, mrc.move, 'r0', 1.2)

    def test_turn(self):
        """Test MarsRoverController turn method."""
        mrc = marsrovercontroller.MarsRoverController(((0, 0, 0), (5, 5, 0)))
        mrc.add_rover('r0', (2, 1, 0), (math.pi/2, math.pi/2))
        #turn left        
        mrc.turn('r0', math.pi/2, 0)
        self.assertEquals(mrc.get_rover('r0').heading, (math.pi, math.pi/2))
        #turn left right       
        mrc.turn('r0', -math.pi/2, 0)
        self.assertEquals(mrc.get_rover('r0').heading, (math.pi/2, math.pi/2))
        #no non orthogonal turning w.r.t. 0 rads        
        self.assertRaises(Exception, mrc.turn, 'r0', -1.1*math.pi/2, 0)


if __name__ == '__main__':
    unittest.main()
