#!/usr/bin/env python
"""
This file is part of a solution to the Mars Rover Exercise.

Matthew Baker <mu.beta.06@gmail.com> 2013

This module defines the base class for the RoverController.

The RoverController is responsible for implementing the rules that govern the
movement of Rovers throughout a given co-ordinate system, moreover, the 
RoverController is responsible for restricting Rover(s) movement. More 
specifically, this implementation of a RoverController sees the restriction of
Rover's movements to orthogonal adjacent unit steps in a grid in a forward only 
direction. In addition to restricting Rover movement the RoverController should 
ensure that Rover's do not collide and, furthermore, do not stray outside the 
nominated co-ordinate system.
"""

import rover


class RoverController(object):

    """This is a base class for describing a RoverController."""

    def __init__(self, gridsize, origin=(0, 0, 0)):
        """Initialise a RoverController."""
        self.rovers = {}
        self._gridsize = gridsize #gridsize should be checked to be positive
        self._origin = origin

    def add_rover(self, rover_id, position, heading):
        """Add a Rover to the RoverController. When a Rover is added the 
        RoverController needs to check that the initial position is not 
        occupied."""
        if self.is_empty(position):
            self.rovers[rover_id] = rover.Rover(position, heading)
        else:
            raise Exception('rover already occupies this position.')

    def move(self, rover_id, distance):
        """The movement of a Rover is differential, i.e. the Rover will be moved
        throughout the co-ordinate space the specified distance from it's 
        current position at it's current heading. In this implementation a Rover 
        can only move in the forward direction a dimensionless integer number of 
        unit lengths. 

        In addition to enforcing these restrictions the RoverController is 
        responsible for appropriately updating the Rovers co-ordinates, ensuring
        that movement of the Rover is not going to see it moving outside of the 
        grid limits and not into another Rover.
        """
        """Might be nice to recursively call this so the Rover steps incrementally.
        Because of the orthogonality restriction all non zero angles must be 
        divisible by pi/2. Also since the Rover can only move in dimensionless
        unit steps we need to ensure that distance is an integer."""
        current_position = self.rovers[rover_id].position
        print current_position

    def turn(self, azimuth, zenith):
        """The turning of a Rover is also differential, i.e. the Rover will be 
        turned from the current heading by the amount specified by Azimuthh and 
        Zenith angles. In this implementation a Rover can only turn orthogonally 
        thus, distance all nonzero Azimuth and Zenith angles must be divisible 
        by pi/2."""
        pass

    def is_empty(self, position):
        """Checks if the specified position is empty or not. Returns True if
        empty otherwise False."""
        for r in self.rovers.values():
            if r.position == position:
                return False
        return True

if __name__ == '__main__':
    controller = RoverController((5, 5, 5))
    controller.add_rover('rover1', (0, 0, 0), (90, 90))
    controller.move('rover1', 4, (0, 0))

