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

FILE_ERROR = 'skeer.err'
FILE_DICT = 'dushi.db'
PATH_DICT = '%s%s%s' % ('/'.join(os.path.realpath(__file__).split('/')[:-1]),'/',FILE_DICT) # wat

DUSHI_ENABLED = True
SMILEY_ENABLED = True
HAXOR_ENABLED = True

class Whollah():
    def __init__(self):
        self.bezem = {}
	
	# gehaltes altijd minimaal 2. hoe lager, hoe dushi'r de zin
	self.DUSHI_GEHALTE = 20
	self.SMILEY_GEHALTE = 3
	self.HAXOR_GEHALTE = 3

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

    def haxor(self, a):
	for k,v in {'e': '3', 'a': '4', 'o': '0', 'i': '1'}.items():
		if k in a and self.bingo(self.HAXOR_GEHALTE):
			a = a.replace(k,v)
	return a

    def dushi(self, a):
        return ''.join(x.upper() if self.bingo(self.DUSHI_GEHALTE) else x for x in a)

    def bingo(self, MAX):
        if randrange(0, MAX) == 1:
            return True

        return False  # :((((((((((

    def kutsmileys(self, a):
        if self.bingo(self.SMILEY_GEHALTE) and self.bezem.has_key('kutsmileys'):
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
	
	# BIJNA KLAAR
        deze = ' '.join(dushi)

        if DUSHI_ENABLED:
	        deze = skeere.dushi(deze)

        if SMILEY_ENABLED:
	        deze = skeere.kutsmileys(deze)
	if HAXOR_ENABLED:
		deze = skeere.haxor(deze)

        # BAM
        print deze
    else:
        # gast, input?
        pass
