import re
from settings import create_dictionary_request

punctuations = re.compile(r'[$&+,:;=?@#|<>.^*()%!-]')
consonants = re.compile('[^aeiou]')
vowels = re.compile('[aeiou]')


# Clean Up Methods
def initial_filter(word: str) -> [str]:
    if re.search(punctuations, word):
        return None
    index = word.find("'")
    if index == -1:
        return word
    else:
        return word[:index]


def extract_nuclei_from_unfiltered(word: str) -> list[str]:
    nuclei = list(filter(None, re.split(consonants, word)))
    return nuclei


def extract_syllables(word: str) -> [list[str]]:
    word = initial_filter(word)
    if not word:
        return None

    nuclei = extract_nuclei_from_unfiltered(word)
    syllabified = create_dictionary_request(word)
    if not syllabified or syllabified.find(' '):
        return None
    syllables = syllabified.split('*')

    if len(syllables) == 1 and len(nuclei) > 1:
        return None
    else:
        return syllables


if __name__ == '__main__':
    print(extract_syllables('alice'))
