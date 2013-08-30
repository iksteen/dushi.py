#!/usr/bin/python
__author__ = "dsc"
__copyright__ = "R&D"
__credits__ = ["Wazakindjes"]
__version__ = "20 aug 2013"
from random import randrange, choice
import argparse
import re
import sys
import os

DUSHI_ENABLED = True
SMILEY_ENABLED = True
HAXOR_ENABLED = True

# gehaltes altijd minimaal 2. hoe lager, hoe meer dushi.
DUSHI_GEHALTE = 8
SMILEY_GEHALTE = 3
HAXOR_GEHALTE = 9

FILE_ERROR = 'skeer.err'
FILE_DICT = 'dushi.db'
PATH_ABS = '/'.join(os.path.realpath(__file__).split('/')[:-1]) + '/'
PATH_DICT = '%s%s' % (PATH_ABS, FILE_DICT)

class Whollah():
    def __init__(self):
        global DUSHI_GEHALTE, SMILEY_GEHALTE, HAXOR_GEHALTE
        self.bezem = {}

        def doe_ding():
            f = open(PATH_DICT)

            for k, v in [z.replace('\n', '').split('=') for z in f.readlines() if z]:
                self.bezem[k] = v.split(',')

            f.close()

        doe_ding()

    def sagbi(self, a): #ewa
        for k, v in self.bezem.items():
            for i in k.split(','):
                if i == a:
                    return v # aw ye
        return None

    def haxor(self, a):
        r = {'e': '3', 'a': '4', 'o': '0', 'i': '1'}

        for k, v in r.items():
            if k in a and self.bingo(HAXOR_GEHALTE):
                a = a.replace(k, v)
        return a

    def dushi(self, a):
        return ''.join(x.upper() if self.bingo(DUSHI_GEHALTE) else x for x in a)

    def bingo(self, MAX):
        if randrange(0, MAX) == 1:
            return True
        return False  # :((((((((((

    def kutsmileys(self, a):
        if self.bingo(SMILEY_GEHALTE) and 'kutsmileys' in self.bezem:
            return '%s %s' % (a, choice(self.bezem['kutsmileys']))
        return a


if __name__ == "__main__":

    p = argparse.ArgumentParser()
    p.add_argument('--dushi', help='dUsHi MOdE ON. Default: %s' % DUSHI_ENABLED, action='store_true')
    p.add_argument('--hax', help='h4x0r m0d3 ON. Default: %s' % HAXOR_ENABLED, action='store_true')
    p.add_argument('--smile', help='smiley mode ON :$:Pp:$. Default: %s' % SMILEY_ENABLED, action='store_true')
    p.add_argument('--update', help='updeet db G', action='store_true')
    p.add_argument('--halp', help='probelm?', action='store_true')
    args, zemmel = p.parse_known_args()

    # args fix
    if len(zemmel) == 1:
        zemmel = ''.join(zemmel).split()

    # check flags
    if args.dushi:
        DUSHI_ENABLED = True
    if args.hax:
        HAXOR_ENABLED = True
    if args.smile:
        SMILEY_ENABLED = True

    if zemmel:
        # werd up
        skeere = Whollah()

        dushi = []
        for w in zemmel:
            chimeid = skeere.sagbi(w.lower()) # zoek ding

            if chimeid:  # jwt
                new = choice(chimeid)

                # oki
                new = new + '.' if w.endswith('.') else new + ',' if w.endswith(',') else new

                # heuelemaal mooi
                dushi.append(new)
            else:
                dushi.append(w)  # :((

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

    elif args.halp:
        print 'https://github.com/nattewasbeer/dushi.py/blob/master/README.md'

    elif args.update:
        import urllib2

        d = [{
                 'uri': 'https://raw.github.com/nattewasbeer/dushi.py/master/dushi.db',
                 'local': FILE_DICT
             }, {
                 'uri': 'https://raw.github.com/nattewasbeer/dushi.py/master/dushi.py',
                 'local': os.path.realpath(__file__).split('/')[-1:][0]
             }
        ]

        for i in d:
            response = urllib2.urlopen(i['uri'])
            f = open(i['local'], 'w')
            f.write(response.read())
            f.close()

            print 'up2deet: %s' % i['local']
    else:
        # gast, input?
        pass
