alphabet = 'abcdefghijklmnopqrstuvwxyz'

def alphabet_position(text):
    if type(text) == str:
        text = text.lower()
        result = ''
        if text.isalpha():
            for letter in text:
                result = result + ' ' + str(alphabet.index(letter) + 1)
            print('only text')
            return result.lstrip(' ')
        else:
            for letter in text:
                if letter.isalpha():
                    result = result + ' ' + str(alphabet.index(letter) + 1)
            print('other symbols')
            return result.lstrip(' ')

if __name__ == '__main__':
    pass
    res = alphabet_position("Thesunsetsetsattwelveoclock")
    print(res)