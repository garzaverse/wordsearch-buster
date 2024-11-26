import argparse
import sys


class CliOptions:
    def __init__(self):
        self.file = None
        self.puzzle = None
        self.min = 3  # Default value for min
        self.max = None

    def parse_args(self):
        parser = argparse.ArgumentParser(description='Process some puzzle options.')

        # Optional arguments
        parser.add_argument('-f', '--file', type=str, help='Specify the file name')
        parser.add_argument('-p', '--puzzle', type=str, help='Specify the puzzle letters')
        parser.add_argument('-m', '--min', type=int, default=3, help='Specify the minimum letters (default: 3)')
        parser.add_argument('-n', '--max', type=int, help='Specify the maximum letters')

        args = parser.parse_args()

        # Ensure that only one of file or puzzle string is present
        if args.file and args.puzzle:
            print('Only one of --file or --puzzle must be provided, not both.', file=sys.stderr)
            sys.exit(1)

        # At least one of file or puzzle string must be provided
        if args.file is None and args.puzzle is None:
            print('At least one of --file or --puzzle must be provided.', file=sys.stderr)
            sys.exit(1)

        # Assign parsed arguments to instance variables
        self.file = args.file
        self.puzzle = args.puzzle
        self.min = args.min
        self.max = args.max
