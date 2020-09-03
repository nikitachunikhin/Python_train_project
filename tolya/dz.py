import string

def strrr(a):
   c = a.capitalize()
   return c

def first_letter_upper(a):
   first_letter = a[0]
   first_letter = first_letter.upper()
   letters = a[1:]
   letters = letters.lower()
   new_string = first_letter + letters
   return new_string


def poz_i(i, example):
   if (i < 0) and (i >= -1 * len(example)):
      poz_i = len(example) + i
   elif (i >= 0) and (i < len(example)):
      poz_i = i
   else:
      poz_i = None
   return poz_i


    #    example = 'knfdjSFj8 78S'
# new = first_letter_upper(example)
# print(new)
#    i = -13
#    k = 0
#
#    #if i<=len(example):
#    #TODO: написать такое условие на (k,i) чтоб result всегда был = True
#    if poz_i(i, example):
#       result = example.endswith(example[i-1], k, i)
#       print(result)
#    else:
#       print('result = False or i - out of string')

   #print(example[len(example)-1])
   # print(len(example))
if __name__ == '__main__':
   output_result = ''
   alfabet = string.ascii_lowercase
   text = "The sunset sets at twelve o' clock."
   text = text.lower()
   for letter in text:
      if letter in alfabet:
         result = alfabet.index(letter) + 1
         result = str(result)
         output_result = output_result + " " + result
   print(output_result)






