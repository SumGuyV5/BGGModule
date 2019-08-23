#!/usr/bin/env python
"""***************************************************************
**  Program Name:   BGGModule				        **
**  Version Number: V0.6                                        **
**  Copyright (C):  September 3, 2014 Richard W. Allen          **
**  Date Started:   September 3, 2014                           **
**  Date Ended:     June 12, 2019                               **
**  Author:         Richardn W. Allen                           **
**  Webpage:        http://www.richardallenonline.com           **
**  IDE:            IDLE 3.7.3                                  **
**  Compiler:       Python 3.7.3                                **
**  Language:        Python 3.7.3				**
**  License:	    GNU GENERAL PUBLIC LICENSE Version 2	**
**		    see license.txt for for details	        **
***************************************************************"""
import sys

sys.path.append('BGGModule.zip')


class PlayerInfo:
    def __init__(self, start_name, start_username):
        self.name = start_name
        self.username = start_username
        self.wincount = 0
        self.losscount = 0
        self.winratio = 0.0
        self.winpercentage = 0.0
        self.gameinfo = []
        self.hIndex = 0
        self.winGameInfo = object()
        self.lossGameInfo = object()

    def load_game_info(self):
        self.gameinfo = sorted(self.gameinfo, key=lambda gameinfo: gameinfo.win, reverse=True)
        self.winGameInfo = self.gameinfo[0]
        self.gameinfo = sorted(self.gameinfo, key=lambda gameinfo: gameinfo.loss, reverse=True)
        self.lossGameInfo = self.gameinfo[0]
        self.gameinfo = sorted(self.gameinfo, key=lambda gameinfo: gameinfo.count, reverse=True)
        count = 0
        while count < self.gameinfo.__len__():
            if self.gameinfo[count].count <= count:
                break
            count += 1
        self.hIndex = count


if __name__ == "__main__":
    pass
