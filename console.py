#!/usr/bin/python3


import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Prompt for an interactive session"""

    def console(self, line):
        """ Prints a custom prompt"""
        if line:
            print("(hbnb)")
        else:
            print("(hbnb)")
    def do_EOF(self, line):
        """prints a newline when prompt is exited"""
        return True

    """
    def create(self, line):
    def show(self, line):
    def destroy(self):
    def all(self):
    def update(self):
    """

if __name__ == '__main__':
    HBNBCommand().cmdloop()
