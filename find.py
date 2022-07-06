import argparse
import re
from soundex import get_soundex
import Levenshtein

# parse command-line arguments
parser = argparse.ArgumentParser(
    description="""CLI tool that finds phrases in a given text file.
    Returns the top unique 5 matched words."""
)
parser.add_argument(
    'file_path',
    help='Text file path.',
)
parser.add_argument(
    'phrase',
    help='Search phrase.')
args = parser.parse_args()


def get_best_match(file_path, phrase):
    """Search for words, soundex codes and levenshtein distance and
    returns the top unique 5 matched words."""
    with open(file_path, encoding='utf-8', ) as file:
        text = file.read()
    rx = re.compile('[^A-Za-z ]+')
    res = rx.sub(' ', text)
    text = res.split(' ')
    text = filter(None, text)
    dict_soundex = {}
    dict_levenshtein = {}
    for word in text:
        if word not in dict_soundex.keys():
            if get_soundex(phrase)[0] == get_soundex(word)[0]:
                value_soundex = get_soundex(word)
                dict_soundex.update({word: value_soundex})
                for key in dict_soundex.keys():
                    value_levenshtein = Levenshtein.distance(phrase, key)
                    dict_levenshtein.update({key: value_levenshtein})
    dict_levenshtein = {k: v for k, v in sorted(dict_levenshtein.items(),
                                                key=lambda item: item[1])}
    print([key for key in dict_levenshtein.keys()][:5])


if __name__ == '__main__':
    get_best_match(args.file_path, args.phrase)