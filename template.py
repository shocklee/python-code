"""
NAME
      this command does things
SYNOPSIS
      command do-things nice
DESCRIPTION
      things are nice when this command does them
AUTHOR
      Mark Shocklee
      
"""

import argparse  #This allows you to run:  program --help

# other stuff

parser = argparse.ArgumentParser(
    description='Path building utility.',
    epilog="""Default operation is to read a list of directory
           names from stdin and print a semi-colon delimited
           path list to stdout.  To terminate --add, --append,
           --prepend or --remove list, use -- as in: {}
           --remove *foo* *bar* -- input.file
           """.format(os.path.basename(sys.argv[0])))
parser.add_argument('--add', '--prepend', 
    help='add specified directories to the front of the path', 
    dest='front', type=str, nargs='+', metavar='DIR', action='append')

# etc.
