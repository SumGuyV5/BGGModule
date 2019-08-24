#!/usr/bin/env python
"""***************************************************************
**  Program Name:   BGGModule				        **
**  Version Number: V0.6                                        **
**  Copyright (C):  September 3, 2014 Richard W. Allen          **
**  Date Started:   September 3, 2014                           **
**  Date Ended:     June 12, 2019                               **
**  Author:         Richard W. Allen                           **
**  Webpage:        http://www.richardallenonline.com           **
**  IDE:            IDLE 3.7.3                                  **
**  Compiler:       Python 3.7.3                                **
**  Language:        Python 3.7.3				**
**  License:	    GNU GENERAL PUBLIC LICENSE Version 2	**
**		    see license.txt for for details	        **
***************************************************************"""
import sys
import datetime

sys.path.append('BGGModule.zip')


class PlaysDataset:
    def __init__(self):
        self.id = 0
        self.gamename = ""
        self.length = 0
        self.location = ""
        self.incomplete = 0
        self.nowinstate = 0
        self.players = []
        self._date = datetime.date.today()

    def add_player(self, player):
        self.players.append(player)

    def find_player_by_name(self, name):
        for i in range(len(self.players)):
            if self.players[i].name == name:
                return i
        return -1

    def date(self, string):
        self._date = datetime.datetime.strptime(string, "%Y-%m-%d")


if __name__ == "__main__":
    pass
