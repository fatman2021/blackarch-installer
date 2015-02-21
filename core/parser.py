#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                                                                              #
# blackarch-installer - Installer for BlackArch Linux                          #
#                                                                              #
# FILE                                                                         #
# parser.py                                                                    #
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
from core.help import Help

# sys imports
import sys
import argparse


class Parser:
    """ command line argument parsing """

    def __init__(self):
        """ init """

        return

    @staticmethod
    def parseArgs():
        """ parse command line arguments """

        parser = argparse.ArgumentParser(usage='%(prog)s -t <arg> [options]',
                add_help=False)
        parser.add_argument(
                '-t',
                metavar='<type>',
                dest='type',
                help='installation type - ? to list all'
                )
        parser.add_argument(
                '-v',
                dest='verbose',
                action='store_true',
                help='increase output verbosity'
                )
        parser.add_argument(
                '-V',
                action='version',
                version='%(prog)s v' +
                VERSION,
                help='print version information'
                )
        parser.add_argument(
                '-H',
                action='help',
                help='print this help message'
                )

        return (parser.parse_args())


# EOF
