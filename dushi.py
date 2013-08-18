#!/usr/bin/python
__author__ = "dsc @ #2600nl @ irc.smurfnet.ch"
__copyright__ = "nope.jpg"
__credits__ = ["Wazakindjes, rawplayer"]  # 1 lobbi!1
__maintainer__ = "Wazakindjes, rawplayer"
__version__ = "17 aug 2013"
from random import randrange
import re
import sys
import os

# whatever
DICT = '%s%s%s' % ('/'.join(os.path.abspath(__file__).split('/')[:-1]),'/','sagbi.txt')

if len(sys.argv) <= 1:
    print 'gast, input?\n'
    sys.exit()

class Whollah():
    global DICT
    def __init__(self):
        self.bezem = {}

        def parse_dict():
            f = open(DICT)
            a = f.readlines()
            f.close()
            for l in a:
                l = l.replace('\n', '').split('=')
                key = l[0]
                value = l[1].split(',')
                self.bezem[key] = value

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
    # werd up
    poepie = Whollah()

    # waz met deze
    zemmel = ' '.join(sys.argv[1::])

    out = []
    for w in zemmel.split():

        # zoek in die ding G
        sletje = poepie.sagbi(re.sub(r'\W+', '', w).lower())

        if sletje:
            # BAM
            new = sletje[randrange(0, len(sletje))]

            # ff die kommas en punten terughalen als ze er waren :@@@@@
            new = [new + '.' if w.endswith('.') else new + ',' if w.endswith(',') else new][0]

            # heuelemaal mooi
            out.append(new)
        else:
            # skeer
            out.append(w)

    # BAM KLAAR OUTPUT ALLES
    breezah = ' '.join(out)

    # ok, nog ff hax0rfyen
    breezah = poepie.haxor(breezah)

    # BAM KLAAR
    print breezah
