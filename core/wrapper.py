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

    def __init__(self):
        """ init """

        return

    @staticmethod
    def msg(message, verbose=False):
        """ print (verbose) message """

        print("[+] " + message)
        if verbose:
            print("    -> " + message)

        return

    @staticmethod
    def warn(msg):
        """ print warning message """

        sys.stderr.write("[!] WARNING: " + msg + "\n")

        return

    @staticmethod
    def error(msg):
        """ print error message and exit """

        sys.stderr.write("[-] ERROR: " + msg + "\n")
        sys.exit(FAILURE)

        return


# EOF
