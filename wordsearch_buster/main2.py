#!/usr/bin/env python3
# encoding: utf-8
from tabulate import tabulate

from cli_options import CliOptions
from wordsearch_buster import WordsearchBuster
from wordsearch_dictionaries import WordsearchDictionaries
from wordsearch_model import WordsearchModel


def main():
    cli_options = CliOptions()
    cli_options.parse_args()

    model = WordsearchModel(min_letters=cli_options.min, max_letters=cli_options.max)
    if cli_options.puzzle:
        model.from_string(cli_options.puzzle)
    elif cli_options.file:
        model.from_file(cli_options.file)

    dicts = WordsearchDictionaries()
    buster = WordsearchBuster(model=model, dicts=dicts)

    print(f'{buster}')
    # headers = list(range(min_letters, num_letters + 1))
    headers = []
    for i in range(model.min_letters, model.max_letters + 1):
        headers.append(f'{i} ({len(buster.answers[i])})')

    print(tabulate(buster.answers, headers=headers, tablefmt='outline'))


if __name__ == '__main__':
    main()
