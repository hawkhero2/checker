import argparse
import pandas
from datetime import datetime

argum_parser = argparse.ArgumentParser(description='Test')

argum_parser.add_argument('--source', type=str, help='Source file')
argum_parser.add_argument('--destination', type=str, help='Destination file')
# http://pymotw.com/2/argparse/

args = argum_parser.parse_args()

try:
    source_df = pandas.read_csv(args.source)
    destination_df = pandas.read_csv(args.destination)

except Exception as e:
    print("\nNo such file.\nCheck the path and try again.\nError Stack:\n")
    print(e)

mydate = datetime.strptime(str(source_df['date'].tail()),'%d/%m/%Y')
print(mydate)