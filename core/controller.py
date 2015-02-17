#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                                                                              #
# blackarch-installer - Installer for BlackArch Linux                          #
#                                                                              #
# FILE                                                                         #
# controller.py                                                                #
#                                                                              #
# DATE                                                                         #
# 2015-02-17                                                                   #
#                                                                              #
# AUTHOR                                                                       #
# Levon 'noptrix' Kayan - <noptrix@nullsecurity.net>                           #
#                                                                              #
################################################################################


# own imports
from core.help import Help
from core.checks import Check
from core.parser import Parser

# sys imports


class Controller:
    """ control program flow routines """

    def __init__(self):
        """ init """

        # command line options, config, etc.
        self.opts = {}

        return

    def start(self):
        """ do first needed things """

        # usage, init, etc.
        Help.banner()
        Check.checkArgc()
        self.opts = vars(Parser.parseArgs())

        return

    def end(self):
        """ do last needed things """

        return


# EOF
