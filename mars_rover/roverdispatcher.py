#!/usr/bin/env python
"""
This file is part of a solution to the Mars Rover Exercise
(http://thefundoowriter.com/2009/10/01/the-mars-rover-problem/).

Matthew Baker <mu.beta.06@gmail.com> 2013

This module defines the base class for the RoverDispatch.

Responsible for interpretting User data into controller data.

"""

class RoverDispatch(object):

    """This is a base for describing a RoverDispatch."""

    def __init__(self):
        """Initialise a RoverDispatch."""

    def turn_left(self):
        """Turn Rover left."""
        pass
        #controller.turn('rover1',  math.pi/2, 0)

    def turn_right(self):
        """Turn Rover Right."""
        pass
        #controller.turn('rover2', -math.pi/2, 0)

    def move(self):
        """Move the nominated Rover forward 1 position."""
        pass
