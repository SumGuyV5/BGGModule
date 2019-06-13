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
from urllib.request import urlretrieve

import time

class DownloadXML:
    def __init__(self, url, filename):
        """init the variables"""
        self.url = url
        self.filename = filename

    def Download(self, url = None, filename = None):
        if url is None:
            url = self.url
        if filename is None:
            filename = self.filename
            
        time.sleep(2)
        print ("Download Starting!")
        print (url)
        urlretrieve(url, filename)
        print ("Download Complete!")

    def DownloadAll(self, url, filename, countto):
        """Returns the number of files download."""
        count = 1
        print ("Download All Starting!")
        while (count <= countto):
            self.Download(url + str(count), filename + str(count) + ".xml")
            count += 1
        print ("Download All Complete!")
        return count

if __name__ == "__main__":
    print ("Testing... DownloadXML Class")
    url = "http://www.boardgamegeek.com/xmlapi2/plays?username=SumGuyV5"
    download = DownloadXML(url)
    download.Download()
