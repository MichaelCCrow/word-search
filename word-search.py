#!/usr/local/bin/python3

# Words source: https://www-personal.umich.edu/~jlawler/wordlist

from argparse import ArgumentParser
from os.path import exists, isdir, expanduser
from os import chdir

if not exists('words.txt'):
    base_dir = expanduser('~/dev/scripts/word-search')
    if not isdir(base_dir):
        print('[ERROR] Base directory not found. Cannot find words.txt')
        exit(1)
    chdir(base_dir)
    if not exists('words.txt'):
        print('[ERROR] Cannot find words.txt')
        exit(1)

parser = ArgumentParser()
# TODO: Implement an alternative search with positional arg 'letters' and mutually exclusive optional [-b,-m,-e] args
# parser.add_argument('letters', type=str, help='Beginning letters of the word')
parser.add_argument('-l', '--length', type=int)
parser.add_argument('-b', '-s', '--start',
                          '--beg', type=str, default='', help='Beginning letters of the word', dest='beg')
parser.add_argument('-m', '--mid', type=str, default='', help='Letters contained in the middle of the word, after any given beginning letters')
parser.add_argument('-e', '--end', type=str, default='', help='Ending letters of the word')
parser.add_argument('-U', '--unscramble', type=str, help='Invoke the Unscrambler on the given letters - can only be used independently or with the --length arg')
args = parser.parse_args()

if args.mid and len(args.mid) < 2:
    print('--mid must be more than one letter')
    exit(1)
if (args.beg or args.mid or args.end) and args.unscramble:
    print('Cannot use positionals [beg, mid, end] with --unscramble argument')
    exit(1)

with open('words.txt', 'r') as words:
    if args.unscramble:
        from unscrambler import Unscrambler
        matches = Unscrambler(words).unscramble(args.unscramble)
    else:
        matches = [word.strip() for word in words
                   if word.strip().startswith(args.beg)
                   and args.mid in word.strip()[len(args.beg):]
                   and word.strip().endswith(args.end)]

for word in matches:
    if args.length is None:
        print(word)
    elif len(word) == args.length:
        print(word)
