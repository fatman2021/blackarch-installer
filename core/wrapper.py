#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                                                                              #
# blackarch-installer - Installer for BlackArch Linux                          #
#                                                                              #
# FILE                                                                         #
# wrapper.py                                                                   #
#                                                                              #
# DATE                                                                         #
# 2015-02-17                                                                   #
#                                                                              #
# AUTHOR                                                                       #
# Levon 'noptrix' Kayan - <noptrix@nullsecurity.net>                           #
#                                                                              #
################################################################################


# own imports
from core.globals import *

# sys imports
import sys


class Wrapper:
    """ class for wrapper methods """

    color = {
                'normal':   '\033[0m',
                'bold':     '\033[1m',
                'white':    '\033[97m',
                'yellow':   '\033[93m',
                'red':      '\033[91m',
                'end':      '\033[0m'
            }

    def __init__(self):
        """ init """

        return

    @staticmethod
    def line(msg, color='normal', bold=False):
        """ print line """

        if bold:
            print(Wrapper.color['bold'] + Wrapper.color[color] + msg +
                    Wrapper.color['end'])
        else:
            print(Wrapper.color[color] + msg + Wrapper.color['end'])

        return

    @staticmethod
    def ask(msg, color='white', verbose=False):
        """ ask for message """

        r = input(Wrapper.color[color] + '[?] ' + msg + Wrapper.color['end'])

        return r

    @staticmethod
    def info(msg, color='white', verbose=False):
        """ print info message """

        if verbose:
            print(Wrapper.color[color] + '    -> ' + msg + Wrapper.color['end'])
        else:
            print(Wrapper.color[color] + '[+] ' + msg + Wrapper.color['end'])

        return

    @staticmethod
    def warn(msg, color='yellow'):
        """ print warning message """

        sys.stderr.write(Wrapper.color[color] + '[!] WARNING: ' + msg +
                Wrapper.color['end'] + '\n')

        return

    @staticmethod
    def error(msg, color='red'):
        """ print error message and exit """

        sys.stderr.write(Wrapper.color[color] + '[-] ERROR: ' + msg +
                Wrapper.color['end'] + '\n')
        sys.exit(FAILURE)

        return


# EOF
