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
from BGGModule.PlaysDataset import PlaysDataset
from BGGModule.PlayerDataset import PlayerDataset
from BGGModule.PlayerInfo import PlayerInfo
from BGGModule.GameInfo import GameInfo
from xml.dom.minidom import parse


class ReadXML:
    def __init__(self):
        self._dom = object
        self.play_count = 0
        self.plays = []
        self.players_info = []

    def read_xml_file(self, filename):
        try:
            self._dom = parse(filename)
        except IOError:
            print(f'File IO Error on file name {filename}.')

        plays_info = self._dom.getElementsByTagName("plays")
        for play_info in plays_info:
            self.play_count = int(play_info.attributes['total'].value)

        for play_tag in self._dom.getElementsByTagName("play"):
            plays_dataset = self._read_xml_plays(play_tag)
            self._read_xml_players(play_tag, plays_dataset)
            self.plays.append(plays_dataset)

    def read_xml_all(self, filename, count_to):
        """Filename only no extension."""
        print("Reading All XML files...")
        for i in range(1, count_to + 1):
            self.read_xml_file(f'{filename}{str(i)}.xml')
        print("Done Reading All XML files...")

    @staticmethod
    def _read_xml_plays(dom):
        rtn = PlaysDataset()
        rtn.id = int(dom.attributes['id'].value)
        rtn.length = int(dom.attributes['length'].value)
        rtn.location = dom.attributes['location'].value
        rtn.incomplete = int(dom.attributes['incomplete'].value)
        rtn.now_in_state = int(dom.attributes['nowinstats'].value)
        rtn.date(dom.attributes['date'].value)
        items = dom.getElementsByTagName("item")
        for item in items:
            rtn.game_name = item.attributes['name'].value

        return rtn

    def _read_xml_players(self, dom, plays_dataset):
        players = dom.getElementsByTagName("player")
        for player in players:
            plays_dataset.add_player(self._load_players(player))

    @staticmethod
    def _load_players(player):
        rtn = PlayerDataset()
        rtn.username = player.attributes['username'].value
        rtn.name = player.attributes['name'].value
        rtn.colour = player.attributes['color'].value
        rtn.win = bool(int(player.attributes['win'].value))
        rtn.new = bool(int(player.attributes['new'].value))
        try:
            rtn.points = int(player.attributes['score'].value)
        except ValueError:
            pass

        return rtn

    def load_info(self):
        self.players_info = []
        for single_play in self.plays:
            if (single_play.incomplete == 0) and (single_play.now_in_state == 0):
                players_points = single_play.points()
                for player in single_play.players:
                    if self._add_player(player.username, player.name, player.win, single_play.game_name,
                                        players_points[player.name]) is False:
                        print("Error Player not found!")
        return self.players_info

    def _add_player(self, username, name, win, game_name, points):
        found = False
        for player_info in self.players_info:
            if (player_info.username == username) and (player_info.name == name):
                found = True
                self._add_game_info(game_name, win, player_info)
                if win is True:
                    player_info.win_count += 1
                else:
                    player_info.loss_count += 1
                player_info.points += points
        if found is False:
            self.players_info.append(PlayerInfo(name, username))
            found = self._add_player(username, name, win, game_name, points)

        return found

    def _add_game_info(self, name, win, player_info):
        found = False
        for game_info in player_info.games_info:
            if game_info.name == name:
                found = True
                game_info.add_count(win)
        if found is False:
            player_info.games_info.append(GameInfo(name))
            found = self._add_game_info(name, win, player_info)
        return found


if __name__ == "__main__":
    print("Testing... ReadXML Class")
    read = ReadXML()

    read.read_xml_file(os.path.join(os.getcwd(), 'plays.xml'))

    for play in read.plays:
        print(f'Name: {play.gamename}')
        """ print f'Username: {player.username}'
        print f'Name: {player.name}'
        print f'Wins: {str(player.wincount)}'
        print f'Loss: {str(player.losscount)}'
        print f'Total Games Played: {str(player.wincount}} {str(player.losscount)}'
        print """
