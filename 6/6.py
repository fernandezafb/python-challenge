
import zipfile


def run_challenge():
    number_file = 90052
    files = zipfile.ZipFile('channel.zip')
    zip_comments = []

    while True:
        file_name = f'{number_file}.txt'

        text = files.read(file_name).decode('utf-8')

        # As the hint found suggests, we have to look at the comment files
        zip_comments.append(files.getinfo(file_name).comment.decode('utf-8'))

        if text.split()[-1].isdigit():
            number_file = text.split()[-1]
        else:
            print(f'The result is: {text}')
            break

    print(''.join(map(lambda comment: f'{comment}', zip_comments)))


if __name__ == '__main__':
    run_challenge()
