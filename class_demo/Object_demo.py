import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text

    # def __getitem__(self, item):
    #     return self.wolds[item]

    def __iter__(self):
        for word in RE_WORD.finditer(self.text):
            yield word.group()

    def __len__(self):
        return len(RE_WORD.findall(self.text))

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word


s = Sentence('"The time has come," the Walrus said,')
print(s)
print(len(s))
for word in s:
    print(word)
