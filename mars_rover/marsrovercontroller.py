#!/usr/bin/env python
"""
This file is part of a solution to the Mars Rover Exercise
(http://thefundoowriter.com/2009/10/01/the-mars-rover-problem/).

Matthew Baker <mu.beta.06@gmail.com> 2013

This module defines an implementation of base class RoverController.

The MarsRoverController implementation of a RoverController sees the restriction 
of Rover's movements to orthogonal adjacent unit steps in a rectangular grid in 
a forward only direction."""

import math

import rovercontroller


class MarsRoverController(rovercontroller.RoverController):

    """This is a specific implementation of base class RoverController."""

    def move(self, rover_id, distance):
        """The movement of a Rover is parametric and differential, i.e. the 
        Rover will be moved throughout the co-ordinate space the specified 
        distance from it's current position at it's current heading. In this 
        implementation a Rover can only move in the forward direction 
        dimensionless integer number of unit lengths. 

        In addition to enforcing these restrictions the RoverController is 
        responsible for appropriately updating the Rovers co-ordinates, ensuring
        that movement of the Rover is not going to see it moving outside of the 
        grid limits and not into another Rover."""
        if not isinstance(distance, int):
            raise Exception('Rover can only move integer units')
        elif distance > 0:
            r = self.get_rover(rover_id)
            x, y, z = r.position
            azimuth, zenith = r.heading
            x += int(math.sin(zenith)*math.cos(azimuth))
            y += int(math.sin(zenith)*math.sin(azimuth))
            z += int(math.cos(zenith))
            self.check_position((x, y, z))
            r.position = (x, y, z)
            self.move(rover_id, distance - 1)
        elif distance < 0:
            raise Exception('Rover can only move in the forward direction')

    def turn(self, rover_id, azimuth, zenith):
        """The turning of a Rover is also differential, i.e. the Rover will be 
        turned from the current heading by the amount specified by Azimuthh and 
        Zenith angles. In this implementation a Rover can only turn orthogonally 
        thus, distance all nonzero Azimuth and Zenith angles must be divisible 
        by pi/2."""
        if azimuth % (math.pi/2) == 0.0 and zenith % (math.pi/2) == 0.0:
            r = self.get_rover(rover_id)
            az, z = r.heading
            az += azimuth
            z += zenith
            r.heading = (az, z)
        else:
            raise Exception('Rover can only turn orthognally')


if __name__ == '__main__':
    controller = MarsRoverController(((0, 0, 0), (5, 5, 0)))
    
    #rover 1
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
    r = controller.get_rover('rover1')
    print r.position, r.heading
    print
    #rover 2
    controller.add_rover('rover2', (3, 3, 0), (0, math.pi/2))
    controller.move('rover2', 1)
    controller.move('rover2', 1)
    controller.turn('rover2', -math.pi/2, 0)
    controller.move('rover2', 1)
    controller.move('rover2', 1)
    controller.turn('rover2', -math.pi/2, 0)
    controller.move('rover2', 1)
    controller.turn('rover2', -math.pi/2, 0)
    controller.turn('rover2', -math.pi/2, 0)
    controller.move('rover2', 1)
    r = controller.get_rover('rover2')
    print r.position, r.heading
