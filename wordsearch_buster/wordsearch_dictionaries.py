class WordsearchDictionaries:
    def __init__(self
                 , words_file='data/words_alpha.txt'
                 , words_addendum='data/words_alpha-addendum.txt'
                 , words_excludes='data/words_alpha-excludes.txt'
                 ):
        self.words_file = words_file
        self.words_addendum = words_addendum
        self.words_excludes = words_excludes

        # read words dictionary
        with open(words_file) as word_file:
            self.words_dict = set(word_file.read().split())

        # read words dictionary addendum
        with open(words_addendum) as word_file:
            self.words_dict_addendum = set(word_file.read().split())

        # combine words dictionary and addendum
        self.words = self.words_dict.union(self.words_dict_addendum)

        # read excludes
        with open(words_excludes) as word_file:
            self.words_dict_excludes = set(word_file.read().split())

    def __repr__(self):
        return f'WordsearchDictionaries(words_file={self.words_file!r}, words_dict={len(self.words_dict)}, words_addendum={len(self.words_dict_addendum)}, words={len(self.words)}, words_excludes={len(self.words_dict_excludes)})'
