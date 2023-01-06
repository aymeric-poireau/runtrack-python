def caesarize_letter(letter):
    if letter == 'S':
        return 'V'
    elif letter == 'A':
        return 'D'
    elif letter == 'L':
        return 'O'
    elif letter == 'U':
        return 'X'
    elif letter == 'T':
        return 'W'
    else:
        return letter

def caesarize(text):
    encoded_letters = []
    for letter in text:
        encoded_letters.append(caesarize_letter(letter))

    return ''.join(encoded_letters)

print(caesarize('SALUT'))