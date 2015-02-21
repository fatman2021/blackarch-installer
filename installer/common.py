#!/usr/bin/env python
# -*- coding: latin-1 -*- ######################################################
#                                                                              #
# blackarch-installer - Installer for BlackArch Linux                          #
#                                                                              #
# FILE                                                                         #
# common.py                                                                    #
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
import subprocess


class BaseInstaller:
    """ installer parent class """

    def __init__(self):
        """ init """

        subprocess.call('clear')

        return



# EOF
