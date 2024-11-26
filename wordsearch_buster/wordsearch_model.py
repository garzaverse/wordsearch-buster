import logging
import re


class WordsearchModel:
    def __init__(self, min_letters=3, max_letters=None):
        self.puzzle = None
        self.filename = None
        self.spec = None
        self.struct = None
        self.answers = []
        self.min_letters = min_letters
        self.max_letters = max_letters
        self.num_letters = None
        self.dictionaries = {}
        self.num_excludes = 0
        self.rows = []

    def from_string(self, puzzle_spec):
        """Sets the puzzle string from a provided string."""
        self.spec = puzzle_spec

        self._parse(puzzle_spec)

    def from_file(self, filename):
        """Reads the puzzle string and answers from a file."""
        self.filename = filename
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if lines:
                    self.spec = lines[0].strip()
                    # self.answers = [line.strip() for line in lines[1:]]
                    self.answers = {line.strip() for line in lines[1:]}

                self._parse(self.spec)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except IOError as e:
            print(f"An error occurred while reading the file '{filename}': {e}")

    def _parse(self, puzzle_spec):
        try:
            # Split the line by the first space to separate the letters from the rest.
            parts = puzzle_spec.split(' ', 1)
            letters = parts[0] if parts else ""
            self.puzzle = re.sub('[^A-Za-z]+', '', letters)  # remove non-alpha
            self.num_letters = len(self.puzzle)

            # Check if there are rows to process
            if len(parts) > 1 and parts[1]:
                self.struct = parts[1] if len(parts) > 1 else ""
                rows_data = parts[1].split(',')
                for row_data in rows_data:
                    character_length, num_rows = map(int, row_data.split(':'))
                    for _ in range(num_rows):
                        self.rows.append(['?'] * character_length)

            if self.max_letters is None:
                self.max_letters = self.num_letters
        except Exception as e:
            logging.error(f"An error occurred while parsing: {e}")

    def __repr__(self):
        return f'WordsearchModel(spec={self.spec!r}, puzzle={self.puzzle!r}, struct={self.struct!r}, answers={self.answers!r}, filename={self.filename!r}, num_letters={self.num_letters!r}, min_letters={self.min_letters!r}, max_letters={self.max_letters})'
