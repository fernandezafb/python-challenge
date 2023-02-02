

def run_challenge():
    """
        a = [1, 11, 21, 1211,
        len(a[30]) = ?
        Link: https://en.wikipedia.org/wiki/Look-and-say_sequence
    """
    number = '1'
    next_number = ''

    # We want to construct 30 numbers to check the length of the last one
    for _ in range(30):
        j = 0
        k = 0

        # j used to track each different digit sequence
        while j < len(number):
            # For a digit sequence, count the digit repetitions in k
            while k < len(number) and number[j] == number[k]:
                k += 1
            # Write the count of the digit + the digit we are counting (11 -> 21)
            # Count is the times the digit appeared - the starting index of the first ocurrence
            next_number += str(k-j) + number[j]
            # Move the j sequence to point to the next different sequence
            j = k

        number = next_number
        next_number = ''

    print(len(number))


if __name__ == '__main__':
    run_challenge()
