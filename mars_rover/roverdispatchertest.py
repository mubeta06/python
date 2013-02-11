#!/usr/bin/env python
"""This file is part of a solution to the Mars Rover Exercise.

Matthew Baker <mu.beta.06@gmail.com> 2013

Unit test for roverdispatcher module.

I have largely omitted tests for type safeness as porting this implementation to 
a type safe language will take care of this.
"""

import math
import unittest

import roverdispatcher
import marsrovercontroller


class TestRoverDispatcher(unittest.TestCase):


    def test_convert_vertices(self):
        """Test converting User Vertices to Controller Vertices."""
        dispatcher = roverdispatcher.RoverDispatcher()
        self.assertEquals(dispatcher.parse_vertex('3 3'), (3, 3, 0))
        self.assertEquals(dispatcher.parse_vertex(' 3 3 '), (3, 3, 0))
        self.assertRaises(ValueError, dispatcher.parse_vertex, 'a b')
        self.assertRaises(ValueError, dispatcher.parse_vertex, ' ')
        self.assertRaises(ValueError, dispatcher.parse_vertex, '5.5 5.5')

    def test_convert_rover(self):
        """Test converting User Rover to Controller Rover."""
        d = roverdispatcher.RoverDispatcher()
        vertices = ((0, 0, 0), (5, 5, 0))
        d.controller = marsrovercontroller.MarsRoverController(vertices)
        d.parse_rover('1 2 N')
        self.assertEquals(d.controller.get_rover('1 2 N').position, (1, 2, 0))
        d.parse_rover(' 2 2 N ')
        self.assertEquals(d.controller.get_rover('2 2 N').position, (2, 2, 0))
        self.assertRaises(Exception, d.parse_rover, '2 2')
        self.assertRaises(ValueError, d.parse_rover, 's 2 N')
        self.assertRaises(ValueError, d.parse_rover, '2.2 2 N')

    def test_convert_instruction(self):
        """Test converting User Instruction to Controller Instruction."""
        d = roverdispatcher.RoverDispatcher()
        vertices = ((0, 0, 0), (5, 5, 0))
        d.parse_instruction('LLMMRR')
        self.assertEquals(d.instructions[0], ['L', 'L', 'M', 'M', 'R', 'R'])
        d.parse_instruction(' LL ')
        self.assertEquals(d.instructions[1], ['L', 'L'])

    def test_dispatch(self):
        """Test unknown instruction."""
        d = roverdispatcher.RoverDispatcher()
        vertices = ((0, 0, 0), (5, 5, 0))
        d.controller = marsrovercontroller.MarsRoverController(vertices)
        d.parse_rover('1 2 N')
        d.parse_instruction(' L L')
        self.assertRaises(Exception, d.dispatch)

    def test_map_user_heading(self):
        """Test mapping of User Heading to Controller Heading."""
        d = roverdispatcher.RoverDispatcher()
        self.assertEquals(d.map_user_heading('N'), math.pi/2)
        self.assertEquals(d.map_user_heading('S'), 3*math.pi/2)
        self.assertEquals(d.map_user_heading('E'), 0)
        self.assertEquals(d.map_user_heading('W'), math.pi)
        self.assertRaises(Exception, d.map_user_heading, 'NW')

    def test_map_controller_heading(self):
        """Test mapping Controller Heading to User Heading."""
        d = roverdispatcher.RoverDispatcher()
        self.assertEquals(d.map_controller_heading(math.pi/2), 'N')
        self.assertEquals(d.map_controller_heading(3*math.pi/2), 'S')
        self.assertEquals(d.map_controller_heading(0), 'E')
        self.assertEquals(d.map_controller_heading(math.pi), 'W')
        self.assertRaises(Exception, d.map_controller_heading, math.pi/4)


if __name__ == '__main__':
    unittest.main()
