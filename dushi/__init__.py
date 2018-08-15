#!/usr/bin/python
from __future__ import print_function

__author__ = "dsc"
__copyright__ = "R&D"
__credits__ = ["Wazakindjes"]
__version__ = "30 aug 2013"
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

class Whollah:
    def __init__(self, db_path, dushi_factor, smiley_factor, haxor_factor):
        self.dushi_factor = dushi_factor
        self.smiley_factor = smiley_factor
        self.haxor_factor = haxor_factor

        self.bezem = {}

        with open(db_path) as f:
            for k, v in [z.replace('\n', '').split('=') for z in f if z]:
                v = v.split(',')
                for a in k.split(','):
                    self.bezem.setdefault(a, []).extend(v)

    def sagbi(self, a): #ewa
        return self.bezem.get(a)

    def haxor(self, a):
        r = {'e': '3', 'a': '4', 'o': '0', 'i': '1'}

        for k, v in r.items():
            if k in a and self.bingo(self.haxor_factor):
                a = a.replace(k, v)
        return a

    def dushi(self, a):
        return ''.join(x.upper() if self.bingo(self.dushi_factor) else x for x in a)

    def bingo(self, MAX):
        if randrange(0, MAX) == 1:
            return True
        return False  # :((((((((((

    def kutsmileys(self, a):
        if self.bingo(self.smiley_factor) and 'kutsmileys' in self.bezem:
            return '%s %s' % (a, choice(self.bezem['kutsmileys']))
        return a

    def __call__(self, a):
        dushi = []
        if self.dushi_factor:
            for w in a.split():
                chimeid = self.sagbi(w.lower()) # zoek ding

                if chimeid:  # jwt
                    new = choice(chimeid)

                    # oki
                    new = new + '.' if w.endswith('.') else new + ',' if w.endswith(',') else new

                    # heuelemaal mooi
                    dushi.append(new)
                else:
                    dushi.append(w)  # :((
        a = ' '.join(dushi)

        # BIJNA KLAAR

        if self.smiley_factor:
            a = self.kutsmileys(a)

        if self.haxor_factor:
            a = self.haxor(a)

        return a


def main():
    global DUSHI_ENABLED, HAXOR_ENABLED, SMILEY_ENABLED
    p = argparse.ArgumentParser()
    p.add_argument('--dushi', help='dUsHi MOdE ON. Default: %s' % DUSHI_ENABLED, action='store_true')
    p.add_argument('--hax', help='h4x0r m0d3 ON. Default: %s' % HAXOR_ENABLED, action='store_true')
    p.add_argument('--smile', help='smiley mode ON :$:Pp:$. Default: %s' % SMILEY_ENABLED, action='store_true')
    p.add_argument('--update', help='updeet db G', action='store_true')
    p.add_argument('--halp', help='probelm?', action='store_true')
    args, zemmel = p.parse_known_args()

    # args fix
    zemmel = ' '.join(zemmel)

    # check flags
    if args.dushi:
        DUSHI_ENABLED = True
    if args.hax:
        HAXOR_ENABLED = True
    if args.smile:
        SMILEY_ENABLED = True

    if zemmel:
        # werd up
        skeere = Whollah(
            PATH_DICT,
            DUSHI_GEHALTE if DUSHI_ENABLED else 0,
            SMILEY_GEHALTE if SMILEY_ENABLED else 0,
            HAXOR_GEHALTE if HAXOR_ENABLED else 0
        )

        # BAM
        print(skeere(zemmel))

    elif args.halp:
        print('https://github.com/nattewasbeer/dushi.py/blob/master/README.md')

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

            print('up2deet: %s' % i['local'])
    else:
        # gast, input?
        pass

if __name__ == "__main__":
    main()
