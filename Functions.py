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
import math
from BGGModule.ReadXML import ReadXML
from BGGModule.DownloadXML import DownloadXML


def play_count(username, pagesize):
    filename = "totalplays.xml"
    path = os.path.join(os.getcwd(), filename)
    url = f'http://www.boardgamegeek.com/xmlapi2/plays?username={username}&pagesize=10'
    if os.path.isfile(path) is False:
        download_xml = DownloadXML(url, filename)
        download_xml.download()

    read_xml = ReadXML()
    print(path)
    read_xml.read_xml_file(path)
    return math.ceil(read_xml.play_count / float(pagesize))
