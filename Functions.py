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
**  Langage:        Python 3.7.3				**
**  License:	    GNU GENERAL PUBLIC LICENSE Version 2	**
**		    see license.txt for for details	        **
***************************************************************"""
import os
import sys
import math

sys.path.append('BGGModule.zip')

from BGGModule.ReadXML import ReadXML
from BGGModule.DownloadXML import DownloadXML


def PlayCount(username, pagesize):
    filename = "totalplays.xml"
    path = os.path.join(os.getcwd(), filename)
    url = "http://www.boardgamegeek.com/xmlapi2/plays?username=" + username + "&pagesize=10"
    if os.path.isfile(path) is False:
        downloadXML = DownloadXML(url, filename)
        downloadXML.Download()

    readXML = ReadXML()
    print (path)
    readXML.ReadXMLFile(path)
    return math.ceil(readXML.playcount / float(pagesize))
