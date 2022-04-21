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
parser.add_argument('letters', type=str, help='Beginning letters of the word')
parser.add_argument('-l', '--length', type=int)

group = parser.add_mutually_exclusive_group()
group.add_argument('-m', '--mid', type=str)
group.add_argument('-e', '--end', type=str)
group.add_argument('-U', '--unscramble', action='store_true')
args = parser.parse_args()

if args.mid and args.end:
    print('Cannot use --mid and --end together')
    exit(1)
elif args.mid and len(args.mid) < 2:
    print('--mid must be more than one letter')
    exit(1)

with open('words.txt', 'r') as words:
    if args.unscramble:
        from unscrambler import Unscrambler
        matches = Unscrambler(words).unscramble(args.letters)
    elif args.end is None and args.mid is None:
        matches = [ word.strip() for word in words if word.startswith(args.letters) ]
    elif args.end:
        matches = [ word.strip() for word in words if word.startswith(args.letters) and word.strip().endswith(args.end) ]
    else: # args.mid
        matches = [ word.strip() for word in words if word.startswith(args.letters) and args.mid in word.strip()[len(args.letters):] ]

for word in matches:
    if args.length is None:
        print(word)
    elif len(word) == args.length:
        print(word)
