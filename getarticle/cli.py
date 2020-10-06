# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import sys
from getarticle import GetArticle
from os.path import expanduser
import sys

def parse_args():
    parser = ArgumentParser(description='getarticle CLI')
    parser.add_argument('-i', '--input', required=False, \
        help='article DOI or website')
    parser.add_argument('-s', '--search', nargs="+", required=False, \
        help='search keywords')
    parser.add_argument('-o', '--output', required=False, \
        help='download direction')
    parser.add_argument('-sd', '--setdirection', required=False, \
        help='set default download direction')
    args = parser.parse_args()
    return args


def main(args):
    if args.setdirection:
        open("%s/.getarticle.ini" %expanduser("~"), "wb").\
            write(args.setdirection.encode())
        return
    ga = GetArticle()
    if not args.input and not args.search:
        if sys.platform == 'darwin':
            import appscript
            args.input = appscript.app("Safari").windows.first.\
                current_tab.URL()
        else:
            raise ValueError("input is required!")
    if args.input:
        ga.input_article(args.input)
    if args.search:
        ga.search(" ".join(args.search))
    ga.download(direction=args.output)


def entry_point():
    args = parse_args()
    main(args)


if __name__ == '__main__':
    entry_point()
