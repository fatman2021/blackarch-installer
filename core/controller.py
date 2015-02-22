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
from core.globals import *
from core.help import Help
from core.checks import Check
from core.wrapper import Wrapper
from core.checks import Check
from core.parser import Parser
from installer.text import TextInstaller
from installer.curses import CursesInstaller

# sys imports
import sys


class Controller:
    """ control program flow routines """

    def __init__(self):
        """ init """

        # command line options, config, etc.
        self.opts = {}

        return

    def start(self):
        """ do first needed things """

        # init, usage, checks, etc.
        Help.banner()
        self.opts = vars(Parser.parseArgs())
        c = Check(self.opts)
        c.checkArgc()
        c.checkArgs()
        c.checkInstallType()

        # run installer here
        if self.opts['type'] == 'text':
            t = TextInstaller(self.opts['verbose'])
            t.run()
        else:
            c = CursesInstaller(self.opts['verbose'])
            c.run()

        return

    def end(self):
        """ do last needed things """

        return


# EOF
