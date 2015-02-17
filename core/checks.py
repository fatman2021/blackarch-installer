#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                                                                              #
# blackarch-installer - Installer for BlackArch Linux                          #
#                                                                              #
# FILE                                                                         #
# cheks.py                                                                     #
#                                                                              #
# DATE                                                                         #
# 2015-02-17                                                                   #
#                                                                              #
# AUTHOR                                                                       #
# Levon 'noptrix' Kayan - <noptrix@nullsecurity.net>                           #
#                                                                              #
################################################################################


# own imports
from core.wrapper import Wrapper

# sys imports
import sys


class Check:
    """ program and command line checks """

    def __init__(self):
        """ init """

        return


    @staticmethod
    def checkArgc():
        """ check argument count """

        if len(sys.argv) == 1:
            Wrapper.error('-H for help and usage')

        return


# EOF
