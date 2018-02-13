import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern', help="Substring pattern")
    parser.add_argument('path', help="File to search in")
    # Boolean arg
    parser.add_argument('-i', '--ignore-case',
                        default=False, action='store_true')
    # Typed Arg
    parser.add_argument('--limit', default=None, type=int,
                        help='Show only this many matches. Default is show all')
    parser.add_argument('-c', '--count', default=False, action='store_true',
                        help='Show only this many matches. Default is show all')

    args = parser.parse_args()
    if args.count and args.limit:
        parser.error('Cannot combine --limit and --count options')
    return args

if __name__ == "__main__":
    args = get_args()
    ## args = parser.parse_args()
    # for line in grepfile(args.pattern, args.path):
    # print(line)
