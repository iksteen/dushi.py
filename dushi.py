#!/usr/bin/python
__author__ = "dsc @ #2600nl @ irc.smurfnet.ch"
__copyright__ = "nope.jpg"
__credits__ = ["Wazakindjes, rawplayer"]  # 1 lobbi!1
__maintainer__ = "Wazakindjes, rawplayer"
__version__ = "18 aug 2013"
from random import randrange
import argparse
import re
import sys
import os

FILE_DICT = 'sagbi.txt'
PATH_DICT = '%s%s%s' % ('/'.join(os.path.abspath(__file__).split('/')[:-1]),'/',FILE_DICT) # wat
	
class Whollah():
    global PATH_DICT

    def __init__(self):
        self.bezem = {}

        def parse_dict():
            f = open(PATH_DICT)
            for l in [z.replace('\n','').split('=') for z in f.readlines() if z]:
                key = l[0]
                value = l[1].split(',')

                self.bezem[key] = value
            f.close()

        parse_dict()

    # ewa
    def sagbi(self, a):
        if not a:
            return None

        for k, v in self.bezem.items():
            for i in k.split(','):
                if i == a:
                    # bam, gevonden die shit
                    return v
            # skeere input
        return None

    def haxor(self, a):
        def bingo():
            # :OOOOOO
            if randrange(0, 6) == 3:
                # BAM
                return True
            # :(((((((((
            return False

        if bingo():
            a = a.replace('e', '3')
        if bingo():
            a = a.replace('a', '4')
        if bingo():
            a = a.replace('o', '0')
        if bingo():
            a = a.replace('i', '1')

        # BAM, ZONNE GROTE KNAL
        return ''.join([''.join([x.upper() if bingo() else x]) for x in list(a)])


if __name__ == "__main__":

	p = argparse.ArgumentParser()
	p.add_argument('--update', help='updeet db G', action='store_true')
	p.add_argument('--halp', help='probelm?', action='store_true')
	args, zemmel = p.parse_known_args()
	
	if args.update:
		import urllib2
		db = 'https://raw.github.com/nattewasbeer/dushi.py/master/sagbi.txt'
		
		response = urllib2.urlopen(db)
		f = open(PATH_DICT,'w')
		f.write(response.read())
		f.close()
	
		print '%s up2date, bam' % FILE_DICT

	elif args.halp:
		print 'https://github.com/nattewasbeer/dushi.py/blob/master/README.md'

	elif zemmel:
	    # werd up
	    skeere = Whollah()

	    out = []
	    for w in zemmel:

		# zoek die ding
		chimeid = skeere.sagbi(re.sub(r'\W+', '', w).lower())

		if chimeid: #jwt
		    new = chimeid[randrange(0, len(chimeid))]

		    # ff die kommas en punten terughalen als ze er waren :@@@@@
		    new = new + '.' if w.endswith('.') else new + ',' if w.endswith(',') else new

		    # heuelemaal mooi
		    out.append(new)
		else:
		    # skeer
		    out.append(w)

	    # BAM KLAAR OUTPUT
	    deze = ' '.join(out)

	    # misscjein nog ff hax0rfyen =]]]
	    deze = skeere.haxor(deze)

	    # BAM
	    print deze
	else:
		# gast, input?
		pass
