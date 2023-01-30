
import urllib.request
import pickle


def http_get(url):
    with urllib.request.urlopen(f'{url}') as response:
        return response.read()


def run_challenge():
    byte_stream_message = http_get('http://www.pythonchallenge.com/pc/def/banner.p')
    banner = pickle.loads(byte_stream_message)

    for tuples in banner:
        print_tuples(tuples)

    # Solution using map and lambda funtion
    for tuples in banner:
        print(''.join(map(lambda tuple: tuple[0] * tuple[1], tuples)))

    # Solution using list comprehension
    for tuples in banner:
        print(''.join([char * count for char, count in tuples]))


def print_tuples(tuples):
    for tuple in tuples:
        for _ in range(tuple[1]):
            print(tuple[0], end='')
    print()


if __name__ == '__main__':
    run_challenge()
