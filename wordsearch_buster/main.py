#!/usr/bin/env python3
# encoding: utf-8

import re
import sys

from tabulate import tabulate


def load_words():
    with open('data/words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    # read extensions
    with open('data/words_alpha-addendum.txt') as word_file:
        more_valid_words = set(word_file.read().split())

    # read excludes
    with open('data/words_alpha-excludes.txt') as word_file:
        excluded_words = set(word_file.read().split())

    return valid_words.union(more_valid_words), excluded_words


def main(argv=None):
    # read dictionary
    english_words, excluded_words = load_words()
    print(f'WORDS: {type(english_words)}, {type(excluded_words)}')

    # get letters from user (or default to command-line)
    if len(sys.argv) > 1:
        user_letters = sys.argv[1]
    else:
        user_letters = input('Enter your letters: ')
    user_letters = re.sub('[^A-Za-z]+', '', user_letters)  # remove non-alpha
    num_letters = len(user_letters)

    min_letters = 3
    if len(sys.argv) > 2:
        print(f'min letters = {min_letters}')
        min_letters = int(sys.argv[2])
    print(f"using '{user_letters}', min_len={min_letters}")

    # split dictionary into dictionaries of [min_letters...num_letters] character words
    dictionaries = {}
    # nb: tabular data type is a dictionary of lists. The key is the word length
    answers = {}
    excluded = 0
    for i in range(min_letters, num_letters + 1):
        # start with empty lists
        dictionaries[i] = []
        answers[i] = []
    for word in english_words:
        if word in excluded_words:
            excluded += 1
            continue
        len_word = len(word)
        if min_letters <= len_word <= num_letters:
            dictionaries[len(word)].append(word)

    # create answer dictionaries where each word can be constructed from user letters
    for i in range(min_letters, num_letters + 1):
        for word in dictionaries[i]:
            letters_left = user_letters
            all_in = True
            for letter in word:
                if letter in letters_left:
                    # remove this letter
                    letters_left = letters_left.replace(letter, '', 1)
                else:
                    all_in = False
            if all_in:
                # all letters in word are in user letters, save it
                answers[i].append(word)

    # find the answer dictionary with the most entries
    # get num_words words found
    # compile list of keys for empty answer dictionaries
    most = 0
    total = 0
    keys_to_remove = []
    for k, v in answers.items():
        if len(v) < 1:
            keys_to_remove.append(k)
        else:
            total += len(v)
            if len(v) > most:
                most = len(v)
    # remove empty answer dictionaries
    for key in keys_to_remove:
        del answers[key]
    for k, v in answers.items():
        answers[k] = sorted(v)

    # sort words in each answer dictionary
    # sorted_answers = {}
    # for k, v in answers.items():
    #     sorted = v.sort()
    #     sorted_answers[k] = sorted
    # endspace = ' '
    # keys = list(answers.keys())
    print(f"CHEATIN WORDS for '{user_letters}', len={num_letters}, words={total}, excluded={excluded}")

    # headers = list(range(min_letters, num_letters + 1))
    headers = []
    # for i in range(min_letters, num_letters + 1):
    #    headers.append(f'{i} ({len(answers[i])})')

    # print(tabulate(answers, headers=headers, tablefmt='outline'))
    print(tabulate(answers, headers=headers, tablefmt='outline'))


if __name__ == '__main__':
    main()
