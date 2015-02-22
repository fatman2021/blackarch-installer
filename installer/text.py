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

    def __init__(self, verbose):
        """ init """

        # holds all user chosen options
        self.opts = {}

        # verbose mode
        self.verbose = verbose

        # calls mom and daddy
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

        Wrapper.line('>> ' + section + '\n\n')

        return

    @staticmethod
    def getInstallMode():
        """ get installation mode """

        count = 0
        answer = ''

        while answer not in ('1', '2', '3'):
            if count >= 1:
                Wrapper.warn('incorrect mode\n')
            Wrapper.info('installation modes:')
            Wrapper.info('1. install from live-iso', verbose=True)
            Wrapper.info('2. install from repository', verbose=True)
            Wrapper.info('3. install from sources using blackman', verbose=True)
            answer = Wrapper.ask('select mode: ')
            count += 1

        return answer

    def run(self):
        """ start here """

        TextInstaller.printHeader()
        TextInstaller.printSection('Welcome to BlackArch Linux Installation!')
        self.opts['mode'] = TextInstaller.getInstallMode()

        return


# EOF
