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
parser.add_argument('-l', '--length', type=int, default=5, help='Only words with this length will be shown. [default:5]')

# group = parser.add_argument_group('Flagged positionals')
# group.add_argument('letters', type=str, help='Letters to search, default assumes beginning letters of the word', default='', nargs='?')
# if not argv[1].startswith('-'):
#     flags = group.add_mutually_exclusive_group(required=True)
#     flags.add_argument('-b', '-s', '--start',
#                              '--beg', action='store_true', help='Words beginning with', dest='beg')
#     flags.add_argument('-m', '--mid', action='store_true', help='Words containing')
#     flags.add_argument('-e', '--end', action='store_true', help='Words ending with')
# else:
# group = parser.add_mutually_exclusive_group(required=True)
# positions = group.add_argument_group('Multiple position search')
parser.add_argument('-b', '-s', '--start',
                          '--beg', type=str, default='', help='Beginning letters of the word', dest='beg')
parser.add_argument('-m', '--mid', type=str, default='', help='Letters contained in the middle of the word, after any given beginning letters')
parser.add_argument('-e', '--end', type=str, default='', help='Ending letters of the word')
parser.add_argument('-U', '--unscramble', type=str, help='Invoke the Unscrambler on the given letters - can only be used independently or with the --length arg')
args = parser.parse_args()

# if args.mid and len(args.mid) < 2:
#     print('--mid must be more than one letter')
#     exit(1)
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
# print(f'------\n{len(matches)}\n------')
