
def load_file(filename):
    with open(filename) as file_object:
        lines = file_object.readlines()

    return lines


def find_rare_characters():
    lines = load_file('2.txt')

    for line in lines:
        for char in line:
            if (64 < ord(char) < 91) or 96 < ord(char) < 123:
                print(char)


if __name__ == '__main__':
    find_rare_characters()
