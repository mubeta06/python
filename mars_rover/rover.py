#!/usr/bin/env python
"""
This file is part of a solution to the Mars Rover Exercise.

Matthew Baker <mu.beta.06@gmail.com> 2013

This module defines the base class for the Rover.

Properties What make a Rover?
-----------------------------
According to the problem specification a Rover has position which is represented 
by a combination of x and y co-ordinates and also a heading which is represented 
by one of the four cardinal compass points 'N' 'S' 'E' 'W'.

Methods What can a Rover do?
----------------------------
According to the problem specification a Rover can turn Left and Right and move 
one grid position in the forward direction.

In reality if one was to build a Rover it is very likely to be able to have more 
degrees of freedom regarding movement. In fact a Rover may even be able to move 
in three dimensions in addition to the two specified in the problem and, 
furthermore, a Rover is likely to be able to move both forward and backwards and
perhaps even sideways. Therefore, it is probably a good idea to make the Rover 
base class as flexible as possible regarding movement and enforce the 
restrictions as specified in the problem at a higher level thus making the Rover 
encapsulation more extensible and reusable on future missions.
"""


class Rover(object):

    """Base class for representing Rover. This implementation of the Rover is 
    going to work on a three dimensioanl Cartisan co-ordinate system in 
    right-hand or positive orientation (as per specified here 
    http://en.wikipedia.org/wiki/Cartesian_coordinate_system). Accordingly, the 
    Rover's position will be indicated using a tuple of 3 (x, y, z). The Rover's
    heading will be represented by a tuple of two angles (Azimuth, Zenith).
    The Azimuth angle will be defined as the angle subtended in a clockwise
    direction from the y axis. The Zenith angle will be defined as the angle 
    subtended in a clockwise angle from the z axis. Both angles will be defined
    in degrees limited to the range 0-360."""

    def __init__(self, position, heading):
        """Initialise a Rover."""
        self.position = position
        self.heading = heading

    def _get_position(self):
        """Return the Rover's position."""
        return self._position

    def _set_position(self, position):
        """Set the Rover's position."""
        if isinstance(position, tuple) and len(position) == 3:
            if (isinstance(position[0], int) and isinstance(position[1], int) 
                and isinstance(position[0], int)):
                self._position = position
            else:
                raise Exception('position must be tuple of ints')
        else:
            raise Exception('position must be tuple of length 3.')

    def _get_heading(self):
        """Return the Rover's heading."""
        return self._heading

    def _set_heading(self, heading):
        """Set the Rover's heading."""
        if isinstance(heading, tuple) and len(heading) == 2:
            if (isinstance(heading[0], int) and isinstance(heading[1], int) and
                0 <= heading[0] <= 360 and 0 <= heading[1] <= 360):
                self._heading = heading
            else:
                raise Exception('heading must be tuple of ints in range 0-360')
        else:
            raise Exception('heading must be tuple of length 2.')

    #properties
    position = property(_get_position, _set_position, None)
    heading = property(_get_heading, _set_heading, None)


if __name__ == '__main__':
    r = Rover((2, 2, 0), (0, 90))
    print r.position
    print r.heading
