#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                                                                              #
# blackarch-installer - Installer for BlackArch Linux                          #
#                                                                              #
# FILE                                                                         #
# text.py                                                                      #
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
from installer.common import BaseInstaller

# sys imports
import subprocess


class TextInstaller(BaseInstaller):
    """ text based installer class """

    def __init__(self):
        """ init """

        BaseInstaller.__init__(self)

        return

    @staticmethod
    def getTermWidth():
        """ get terminal width """

        cmd = ['tput', 'cols']

        return int(subprocess.check_output(cmd))

    @staticmethod
    def printHeader():
        """ print header """

        Wrapper.line('-' * TextInstaller.getTermWidth(), color='red', bold=True)
        Wrapper.line('--==[ blackarch-installer ]==--', color='white', bold=True)
        Wrapper.line('-' * TextInstaller.getTermWidth(), color='red', bold=True)
        print('\n')

        return

    @staticmethod
    def printSection(section):
        """ print section heading message """

        Wrapper.line('>> ' + section)
        print('\n')

        return


# EOF
