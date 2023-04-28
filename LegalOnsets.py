# import nltk
# nltk.download("brown")

# from nltk.corpus import brown
from Tree import Node
from FilterMethods import extract_syllables, vowels
import re


# Save legal onsets
def get_onset(syllable: str) -> [str]:
    match = re.search(vowels, syllable)
    if match:
        return syllable[:match.start()]
    else:
        y_index = syllable.find('y')
        if y_index == -1:
            return None
        else:
            return syllable[:y_index]


def is_onset_legal(root: Node, onset: str):
    curr = root
    for char in onset:
        flag = False
        for child in curr.children:
            if char == child.data:
                curr = child
                flag = True
                break
        if not flag:
            return False
    return True


if __name__ == '__main__':
    # # List of words to feed the algorithm
    # words = brown.words(categories='news')
    # for word in words:
    #     syllables = extract_syllables(word)
    #     if not syllables:
    #         continue

    print(get_onset('fry'))
