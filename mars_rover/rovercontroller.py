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

import math

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
            raise Exception('A Rover already occupies this position.')

    def move(self, rover_id, distance):
        """The movement of a Rover is differential, i.e. the Rover will be moved
        throughout the co-ordinate space the specified distance from it's 
        current position at it's current heading. In this implementation a Rover 
        can only move in the forward direction a dimensionless integer number of 
        unit lengths. 

        In addition to enforcing these restrictions the RoverController is 
        responsible for appropriately updating the Rovers co-ordinates, ensuring
        that movement of the Rover is not going to see it moving outside of the 
        grid limits and not into another Rover."""

        r = self.rovers[rover_id]
        x, y, z = r.position
        print x, y, z
        if (distance > 0):
            x += int(math.sin(r.zenith)*math.cos(r.azimuth))
            y += int(math.sin(r.zenith)*math.sin(r.azimuth))
            z += int(math.cos(r.zenith))
            if self.is_empty((x, y, z)):
                r.position = (x, y, z)
                self.move(rover_id, distance - 1)
            else:
                raise Exception('A Rover already occupies this position.')
        

    def turn(self, rover_id, azimuth, zenith):
        """The turning of a Rover is also differential, i.e. the Rover will be 
        turned from the current heading by the amount specified by Azimuthh and 
        Zenith angles. In this implementation a Rover can only turn orthogonally 
        thus, distance all nonzero Azimuth and Zenith angles must be divisible 
        by pi/2."""
        if azimuth % (math.pi/2) == 0.0 and zenith % (math.pi/2) == 0.0:
            r = self.rovers[rover_id]
            az = r.azimuth
            z = r.zenith
            az += azimuth
            z += zenith
            r.heading = (az, z)
            #mod 2pi??
        else:
            raise Exception('Rover can only turn orthognally')

    def is_empty(self, position):
        """Checks if the specified position is empty or not. Returns True if
        empty otherwise False."""
        for r in self.rovers.values():
            if r.position == position:
                return False
        return True

if __name__ == '__main__':
    controller = RoverController((5, 5, 5))
    controller.add_rover('rover1', (1, 2, 0), (math.pi/2, math.pi/2))
    controller.turn('rover1',  math.pi/2, 0)
    controller.move('rover1', 1)
    controller.turn('rover1',  math.pi/2, 0)
    controller.move('rover1', 1)
    controller.turn('rover1',  math.pi/2, 0)
    controller.move('rover1', 1)
    controller.turn('rover1',  math.pi/2, 0)
    controller.move('rover1', 1)
    controller.move('rover1', 1)

