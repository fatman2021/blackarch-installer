#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                                                                              #
# blackarch-installer - Installer for BlackArch Linux                          #
#                                                                              #
# FILE                                                                         #
# curses.py                                                                    #
#                                                                              #
# DATE                                                                         #
# 2015-02-17                                                                   #
#                                                                              #
# AUTHOR                                                                       #
# Levon 'noptrix' Kayan - <noptrix@nullsecurity.net>                           #
#                                                                              #
################################################################################


# own imports
from installer.common import BaseInstaller

# sys imports


class CursesInstaller(BaseInstaller):
    """ curses based installer class """

    def __init__(self, verbose):
        """ init """

        self.verbose = verbose
        BaseInstaller.__init__(self)

        return

    def run(self):
        """ start here """

        return


# EOF
