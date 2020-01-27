from collections import defaultdict

class LetterAttr:
    def __getattr__(self, name):
        return name

    def __setattr__(self, name, val):
        object.__setattr__(self, name, ''.join([l for l in val if l in set(name)]))
