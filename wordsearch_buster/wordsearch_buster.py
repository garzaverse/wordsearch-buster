class WordsearchBuster:
    def __init__(self, model, dicts):
        self.model = model
        self.dicts = dicts
        self.dictionaries = {}
        self.answers = {}
        self.num_excluded = 0
        self.num_words = 0

        min_letters = self.model.min_letters
        max_letters = self.model.max_letters
        puzzle = model.puzzle

        # split dictionary into dictionaries of [min_letters...num_letters] character words
        # nb: tabular data type is a dictionary of lists. The key is the word length
        for i in range(min_letters, max_letters + 1):
            # start with empty lists
            self.dictionaries[i] = []
            self.answers[i] = []
        for word in dicts.words:
            if word in self.dicts.words_dict_excludes:
                self.num_excluded += 1
                continue
            len_word = len(word)
            if min_letters <= len_word <= max_letters:
                self.dictionaries[len(word)].append(word)

        # create answer dictionaries where each word can be constructed from user letters
        for i in range(min_letters, max_letters + 1):
            for word in self.dictionaries[i]:
                letters_left = puzzle
                all_in = True
                for letter in word:
                    if letter in letters_left:
                        # remove this letter
                        letters_left = letters_left.replace(letter, '', 1)
                    else:
                        all_in = False
                if all_in:
                    # all letters in word are in user letters, save it
                    self.answers[i].append(word)

        # find the answer dictionary with the most entries
        # get num_words words found
        # compile list of keys for empty answer dictionaries
        most = 0
        self.num_words = 0
        keys_to_remove = []
        for k, v in self.answers.items():
            if len(v) < 1:
                keys_to_remove.append(k)
            else:
                self.num_words += len(v)
                if len(v) > most:
                    most = len(v)
        # remove empty answer dictionaries
        for key in keys_to_remove:
            del self.answers[key]
        for k, v in self.answers.items():
            self.answers[k] = sorted(v)

    def __repr__(self):
        return f'WordsearchBuster(model={self.model!r}, dicts={self.dicts!r}, dictionaries={self.dictionaries.keys()!r}, answers={self.answers.keys()!r}, num_excluded={self.num_excluded!r}, num_words={self.num_words!r})'

    def __str__(self):
        return f'WordsearchBuster(puzzle={self.model.puzzle}({len(self.model.puzzle)}), num_words={self.num_words}, num_excluded={self.num_excluded})'