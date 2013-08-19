#!/usr/bin/python
__author__ = "dsc"
__copyright__ = "MIT"
__credits__ = ["Wazakindjes"]
__version__ = "19 aug 2013"
from random import randrange,choice
import argparse
import re
import sys
import os

FILE_DICT = 'dushi.db'
PATH_DICT = '%s%s%s' % ('/'.join(os.path.realpath(__file__).split('/')[:-1]),'/',FILE_DICT) # wat

DUSHI_ENABLED = True
SMILEY_ENABLED = True

DUSHI_GEHALTE = 8  # HOE LAGER, HOE MEER DUSHI! 2 minimaal.
SMILEY_GEHALTE= 3  # HOE LAGER, HOE MEER SMILEYS! 2 minimaal.

class Whollah():
    global PATH_DICT

    def __init__(self):
        self.bezem = {}

        def doe_ding():
            f = open(PATH_DICT)

            for k, v in [z.replace('\n','').split('=') for z in f.readlines() if z]:
                self.bezem[k] = v.split(',')

            f.close()

        doe_ding()

    def sagbi(self, a): #ewa
        if not a:
            return None

        for k, v in self.bezem.items():
            for i in k.split(','):
                if i == a:
                    return v # aw ye
        return None

    def dushi(self, a):
        if self.bingo(True):
            a = a.replace('e', '3')
        if self.bingo(True):
            a = a.replace('a', '4')
        if self.bingo(True):
            a = a.replace('o', '0')
        if self.bingo(True):
            a = a.replace('i', '1')

        # ZONNE GROTE KNAL
        return ''.join(x.upper() if self.bingo(True) else x for x in a)

    def bingo(self, b):
        global DUSHI_GEHALTE, SMILEY_GEHALTE

        if b:
            if randrange(0, DUSHI_GEHALTE) == 1:
                return True

        else:
            if randrange(0, SMILEY_GEHALTE) == 1:
                return True

        return False  # :((((((((((

    def kutsmileys(self, a):
        if self.bingo(False) and self.bezem.has_key('kutsmileys'):
            return '%s %s' % (a, choice(self.bezem['kutsmileys']))

        return a

if __name__ == "__main__":

    p = argparse.ArgumentParser()
    p.add_argument('--update', help='updeet db G', action='store_true')
    p.add_argument('--halp', help='probelm?', action='store_true')
    args, zemmel = p.parse_known_args()

    if len(zemmel) == 1:
        zemmel = ''.join(zemmel).split() # args fix

    if args.update:
        import urllib2
        db = 'https://raw.github.com/nattewasbeer/dushi.py/master/dushi.db'

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

        dushi = []
        for w in zemmel:

            # zoek ding
            chimeid = skeere.sagbi(re.sub(r'\W+', '', w).lower())

            if chimeid: # jwt
                new = chimeid[randrange(0, len(chimeid))]

                # oki
                new = new + '.' if w.endswith('.') else new + ',' if w.endswith(',') else new

                # heuelemaal mooi
                dushi.append(new)
            else:
                # :((
                dushi.append(w)

        # EINDELIJK KLAAR
        deze = ' '.join(dushi)

        if DUSHI_ENABLED:
	        deze = skeere.dushi(deze)

        if SMILEY_ENABLED:
	        deze = skeere.kutsmileys(deze)

        # BAM
        print deze
    else:
        # gast, input?
        pass
