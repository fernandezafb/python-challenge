
import urllib.request
import urllib.parse


def http_get(url, params=None):
    data = urllib.parse.urlencode(params)
    with urllib.request.urlopen(f'{url}?%s' % data) as response:
        return response.read().decode('utf-8')


def retrieve_final_message(message):
    return [int(word) for word in message.split() if word.isdigit()]


def find_solution():
    nothing = 8022
    while True:
        response = http_get('http://www.pythonchallenge.com/pc/def/linkedlist.php', params={'nothing': nothing})
        numbers = retrieve_final_message(response)

        print(numbers)

        if not numbers:
            return response
        nothing = numbers[0]


if __name__ == '__main__':
    print(find_solution())
