#!/usr/bin/python3

# LagunaGFX
# VimWiki maintenance script
# applied to my Watch List
#
# Changelog :
# - 2024.10.09 1st draft
#
# Comments :
# uses pathlib to obtain a valid $HOME directory path

from pathlib import Path
from urllib.request import urlopen
from bs4 import BeautifulSoup

home = Path.home()

# open file in read mode
with open( home / 'Documentos' / 'Wiki' / 'leisure'/ 'watch.md', 'r') as source :
    with open( home / 'Documentos' / 'Wiki' / 'leisure'/ 'watch_parsed.md', 'w') as destination : 
        for line in source :
            if line.strip().find("https://www.youtube.com/watch") == 0 :
            #if "https://www.youtube.com/" in line.strip():
                url = line.strip()
                soup = BeautifulSoup(urlopen(url),'lxml')
                parsed =  "- [ ] [" + soup.title.get_text().replace(' - YouTube','') + "](" + url + ")\n"
            else:
                if len(line.strip()) > 0 :
                    parsed = line.strip() + "\n"
                else:
                    parsed = "\n"
            print( parsed.strip() )
            destination.write( parsed )
    destination.close()
source.close()
