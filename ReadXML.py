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
import os
import sys

from BGGModule.PlaysDataset import PlaysDataset
from BGGModule.PlayerDataset import PlayerDataset

from xml.dom.minidom import parse

sys.path.append('BGGModule.zip')


class ReadXML:
    def __init__(self):
        self._dom = object
        self.play_count = 0
        self.plays = []

    def read_xml_file(self, filename):
        try:
            self._dom = parse(filename)
        except IOError:
            print(f'File IO Error on file name {filename}')

        plays_info = self._dom.getElementsByTagName("plays")
        for play_info in plays_info:
            self.play_count = int(play_info.attributes['total'].value)

        for play in self._dom.getElementsByTagName("play"):
            playsdataset = self._read_xml_plays(play)
            self._read_xml_players(play, playsdataset)
            self.plays.append(playsdataset)

    def read_xml_all(self, filename, countto):
        """Filename only no extension."""
        print("Reading All XML files...")
        for i in range(1, countto + 1):
            self.read_xml_file(filename + str(i) + ".xml")
        print("Done Reading All XML files...")

    @staticmethod
    def _read_xml_plays(dom):
        rtn = PlaysDataset()
        rtn.id = int(dom.attributes['id'].value)
        rtn.length = int(dom.attributes['length'].value)
        rtn.location = dom.attributes['location'].value
        rtn.incomplete = int(dom.attributes['incomplete'].value)
        rtn.nowinstate = int(dom.attributes['nowinstats'].value)
        rtn.date(dom.attributes['date'].value)
        items = dom.getElementsByTagName("item")
        for item in items:
            rtn.gamename = item.attributes['name'].value

        return rtn

    def _read_xml_players(self, dom, playsdataset):
        players = dom.getElementsByTagName("player")
        for player in players:
            playsdataset.add_player(self._load_players(player))

    @staticmethod
    def _load_players(player):
        rtn = PlayerDataset()
        rtn.username = player.attributes['username'].value
        rtn.name = player.attributes['name'].value
        rtn.colour = player.attributes['color'].value
        rtn.win = bool(int(player.attributes['win'].value))
        rtn.new = bool(int(player.attributes['new'].value))

        return rtn


if __name__ == "__main__":
    print("Testing... ReadXML Class")
    read = ReadXML()

    read.read_xml_file(os.path.join(os.getcwd(), 'plays.xml'))

    for play in read.plays:
        print("Name: " + play.gamename)
        """ print f'Username: {player.username}'
        print f'Name: {player.name}'
        print f'Wins: {str(player.wincount)}'
        print f'Loss: {str(player.losscount)}'
        print f'Total Games Played: {str(player.wincount}} {str(player.losscount)}'
        print """
