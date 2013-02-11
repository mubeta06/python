#!/usr/bin/env python
"""
This file is part of a solution to the Mars Rover Exercise
(http://thefundoowriter.com/2009/10/01/the-mars-rover-problem/).

Matthew Baker <mu.beta.06@gmail.com> 2013

This module defines the base class for the RoverController.

The RoverController is responsible for implementing the rules that govern the
movement of Rovers throughout a given co-ordinate system, moreover, the 
RoverController is responsible for restricting Rover(s) movement. In addition to 
restricting Rover movement the RoverController should ensure that Rover's do not 
collide and, furthermore, do not stray outside the nominated co-ordinate system.

If co-ordinate translation is required a affine matrix can be layered onto 
either side of this Controller.
"""

import math

import rover


class RoverController(object):

    """This is a base class for describing a RoverController."""

    def __init__(self, vertices):
        """Initialise a RoverController. The RoverController is initialised with
        two diagonal vertices. For example ((0, 0, 0), (5, 5, 5)) or 
        ((0, 0, 0), (5, -5, 0))."""
        self.rovers = {}
        self.vertices = vertices

    def add_rover(self, rover_id, position, heading):
        """Add a Rover to the RoverController. When a Rover is added the 
        RoverController needs to check that the initial position is not 
        occupied and rover id is unique."""
        self.check_position(position)
        if not rover_id in self.rovers.keys():
            self.rovers[rover_id] = rover.Rover(position, heading)
        else:
            raise Exception('A Rover with id %s already exists' % str(rover_id))

    def get_rover(self, rover_id):
        """Return the Rover object associated with rover_id."""
        if not rover_id in self.rovers.keys():
            raise Exception('Rover %s could not be found' % str(rover_id))
        else:
            return self.rovers[rover_id]

    def move(self, rover_id, distance):
        """Stub method for moving Rover to be overridden in subclass 
        implementation."""
        pass

    def turn(self, rover_id, azimuth, zenith):
        """Stub method for turning Rover to be overridden in subclass 
        implementation."""
        pass

    def is_empty(self, position):
        """Checks if the specified position is empty or not. Returns True if
        empty otherwise False."""
        return (False if position in [r.position for r in self.rovers.values()] 
                else True)

    def in_grid(self, position):
        """Checks if the specified position is within the legal constraints of 
        the imposed grid. Returns True if position is within grid False 
        otherwise."""
        x, y, z = position
        return (True if ((self.vertices[0][0] <= x <= self.vertices[1][0] or
                        self.vertices[1][0] <= x <= self.vertices[0][0]) and 
                        (self.vertices[0][1] <= y <= self.vertices[1][1] or
                        self.vertices[1][1] <= y <= self.vertices[0][1]) and 
                        (self.vertices[0][2] <= z <= self.vertices[1][2] or
                        self.vertices[1][2] <= z <= self.vertices[0][2])) 
                else False)

    def check_position(self, position):
        """Checks the specified position raising the appropriate exception if
        position is illegal."""
        if not isinstance(position, tuple) and len(vertices) == 3:
            raise Exception('position must be tuple of length 3.')
        if not (isinstance(position[0], int) and isinstance(position[1], int) 
            and isinstance(position[2], int)):
            raise Exception('positions must be integers.')
        if not self.is_empty(position):
            raise Exception('Rover already occupies %s' % str(position))
        elif not self.in_grid(position):
            raise Exception('Position %s is out of grid' % str(position))

    def _get_vertices(self):
        """Return the RoverController's vertices."""
        return self._vertices

    def _set_vertices(self, vertices):
        """Set the RoverController's vertices."""
        if isinstance(vertices, tuple) and len(vertices) == 2:
            if (isinstance(vertices[0], tuple) and len(vertices[0]) == 3 and 
                isinstance(vertices[1], tuple) and len(vertices[1]) == 3):
                self._vertices = vertices
            else:
                raise Exception('vertex must be tuple of length 3.')            
        else:
            raise Exception('vertices must be tuple of length 2.')

    #properties
    vertices = property(_get_vertices, _set_vertices, None)


if __name__ == '__main__':
    controller = RoverController(((0, 0, 0), (5, 5, 0)))
    
    #rover 1
    controller.add_rover('rover1', (1, 2, 0), (math.pi/2, math.pi/2))
    r = controller.get_rover('rover1')
    print r.position, r.heading
    print
    #rover 2
    controller.add_rover('rover2', (3, 3, 0), (0, math.pi/2))
    r = controller.get_rover('rover2')
    print r.position, r.heading
