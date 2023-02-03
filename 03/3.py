import re

from itertools import groupby


def load_file(filename):
    with open(filename) as file_object:
        lines = file_object.readlines()

    return ''.join(lines)


def find_rare_characters():
    text = load_file('3.txt')

    letters = {}
    for char in text:
        letters[char] = letters.get(char, 0) + 1

    # This is just an example of grouping, not used in the final solution
    groups = groupby(text)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    ", ".join("{}x{}".format(label, count) for label, count in result)

    # Solution starts here
    print(''.join(re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', text)))


if __name__ == '__main__':
    find_rare_characters()
