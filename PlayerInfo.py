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


class PlayerInfo:
    def __init__(self, start_name, start_username):
        self.name = start_name
        self.username = start_username
        self.wincount = 0
        self.losscount = 0
        self.winratio = 0.0
        self.gameinfo = []
        self.hIndex = 0
        self.winGameInfo = None
        self.lossGameInfo = None
        self.points = 0

    def win_ratio(self):
        """
        This calculates the loss ratio.
        :return:
        """
        if (self.wincount != 0) and (self.losscount != 0):
            self.winratio = round(float(self.losscount) / float(self.wincount), 2)

    @property
    def win_percentage(self):
        """
        This calculates the percentage of wins to losses.
        :return:
        """
        return 100 * float(self.wincount) / float(self.wincount + self.losscount)

    def win_info(self):
        """
        This finds out what game you have the most wins in.
        :return:
        """
        self.gameinfo = sorted(self.gameinfo, key=lambda gameinfo: gameinfo.win, reverse=True)
        self.winGameInfo = self.gameinfo[0]

    def loss_info(self):
        """
        This finds out what game you have the most losses in.
        :return:
        """
        self.gameinfo = sorted(self.gameinfo, key=lambda gameinfo: gameinfo.loss, reverse=True)
        self.lossGameInfo = self.gameinfo[0]

    def h_index(self):
        """
        This is finds out your h-index.
        :return:
        """
        self.gameinfo = sorted(self.gameinfo, key=lambda gameinfo: gameinfo.count, reverse=True)
        for idx, info in enumerate(self.gameinfo):
            if info.count <= idx:
                self.hIndex = idx
                break

    def load_game_info(self):
        """
        This method finds out how many games you have won, lost and your h-index
        :return:
        """
        self.win_ratio()
        self.win_percentage()
        self.win_info()
        self.loss_info()
        self.h_index()


if __name__ == "__main__":
    pass
