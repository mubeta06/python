#!/usr/bin/env python
"""
This file is part of a solution to the Mars Rover Exercise.

Matthew Baker <mu.beta.06@gmail.com> 2013

This module defines the base class for the RoverController.

The RoverController is responsible for implementing the rules that govern the
movement of Rovers throughout a given co-ordinate system. The RoverController 
should ensure that Rover's do not collide and, furthermore, do not stray outside
the nominated co-ordinate system. In order to accomplish this a RoverController
must possess a container of Rover objects.
"""


class RoverController(object):

    """This is a base class for describing a RoverController."""

    def __init__(self):
        """Initialise a RoverController."""
        self.rovers = []
        origin = (0, 0, 0)
        gridsize = (0, 0, 0)

    def add_rover(self):
        """Add a Rover to the RoverController."""
        #when a Rover is added one needs to specify a position and heading. The
        #appropriate checks can be made here

    def move(self, rover, distance):
        """This method will be responsable for appropriately updating it's
        co-ordinate."""

    def turn(self, theta):
        """This method simply sets the Rover's heading."""

