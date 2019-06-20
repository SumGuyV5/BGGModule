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
    def __init__(self, url = None, filename = None):
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
        ''' "url" = web url to the xml file
            "filename" = the filename for the xml files, don't add .xml.
            "coutto" how many xml files to download.'''
        print ("Download All Starting!")
        for i in range(1,countto):
            self.Download(url + str(i), filename + str(i) + ".xml")
        print ("Download All Complete!")

if __name__ == "__main__":
    print ("Testing... DownloadXML Class")
    url = "http://www.boardgamegeek.com/xmlapi2/plays?username=SumGuyV5"
    download = DownloadXML(url)
    download.Download()
