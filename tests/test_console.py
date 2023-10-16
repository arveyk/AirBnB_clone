#!/usr/bin/python3
""" unittest module for console programm"""

import unittest
from console import Console


class TestConsole(unittest.TestCase):
    """ Test casses for testing console function
    """
    pass

with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
