import re
import string

def alphabet_position(text):
    alfabet = string.ascii_lowercase
    output_result = ''
    text = re.sub("[^a-zA-Z]+", "", text)
    text = text.lower()
    for letter in text:
        result = alfabet.index(letter) + 1
        result = str(result)
        output_result = output_result + result + " "
    output_result = output_result.strip()
    return output_result

if __name__ == '__main__':
    pass
    res = alphabet_position("The sunset sets at twelve o' clock.")
    print(res)