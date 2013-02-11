#!/usr/bin/env python
"""This file is part of a solution to the Mars Rover Exercise.

Matthew Baker <mu.beta.06@gmail.com> 2013

Integration test for Mars Rover solution.

"""

import math
import unittest

import roverdispatcher


class RoverIntegrationTest(unittest.TestCase):


    def test_end_to_end(self):
        """Tests the Mars Rover Solution End to End for given test data."""
        input = '5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM'
        output = '1 3 N\n5 1 E\n'
        dispatcher = roverdispatcher.RoverDispatcher()
        dispatcher.parse_input(input)
        dispatcher.dispatch()
        self.assertEquals(dispatcher.render_view(), output)

    #add more test cases...


if __name__ == '__main__':
    unittest.main()
