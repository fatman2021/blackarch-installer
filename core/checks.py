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
from core.globals import *
from core.wrapper import Wrapper

# sys imports
import sys


class Check:
    """ program and command line checks """

    def __init__(self, opts):
        """ init """

        self.opts = opts

        return

    def checkArgc(self):
        """ check command line argument count """

        if len(sys.argv) == 1:
            Wrapper.error('-H for help and usage')

        return

    def checkArgs(self):
        """ check command line arguments """

        if not self.opts['type']:
            Wrapper.error('-t not given')

        return

    def checkInstallType(self):
        """ check chosen installation type or list available types """

        types = ['text', 'curses']

        if self.opts['type'] == '?':
            Wrapper.info('supported installation types', color='normal')
            Wrapper.info('text', color='normal', verbose=True)
            Wrapper.info('curses', color='normal', verbose=True)
            sys.exit(SUCCESS)

        if self.opts['type'] not in types:
            Wrapper.error('unknown installation type: ' + self.opts['type'])

        return


# EOF
