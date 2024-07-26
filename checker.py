import subprocess
import argparse

argum_parser = argparse.ArgumentParser(description='Test')

argum_parser.add_argument('--source', type=str, help='Source file')
argum_parser.add_argument('--destination', type=str, help='Destination file')
argum_parser.add_argument('--help', type=str, help='Destination file')
# http://pymotw.com/2/argparse/

args = argum_parser.parse_args()

source = args.source
destination = args.destination
help = args.help

if help != None:
    print(help)