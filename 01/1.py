
def decipher_message(message):
    new_message = ''
    for char in message:
        if is_blank(char) or ord(char) > 122 or ord(char) < 97:
            new_message += char
        else:
            new_char = ord(char) + 2
            if new_char > 122:
                new_char -= 26
            new_message += chr(new_char)

    print(new_message)


def is_blank(string):
    return not (string and string.strip())


if __name__ == '__main__':
    decipher_message('g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq '
                     'glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu '
                     'ynnjw ml rfc spj.')
