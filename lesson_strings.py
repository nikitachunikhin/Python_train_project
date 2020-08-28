str1 = 'hello'
str2 = "hello"

str3 = "I don't have a dog"

str4 = "I don't have a dog"

str5 = 'I don"t have a dog'

str6 = 'I don"t have a dog 565465 6546545'


#               'h   e   l   l   o'
# index          0   1   2   3   4
# reverse index  -5  -4  -3  -2 -1

#print(str1[4])
#print(str1[-1])


# Slicing
# string[start:stop:step]
# including start not including stop!

# for example:
# alphabet[8]
# Out[31]: 'i'
# alphabet[2:8:]
# Out[32]: 'cdefgh'


#alphabet = "abcdefghijklmnopqrst"
# alphabet
# Out[15]: 'abcdefghijklmnopqrst'
# alphabet[::]
# Out[16]: 'abcdefghijklmnopqrst'
# alphabet[::1]
# Out[17]: 'abcdefghijklmnopqrst'

# alphabet[::2]
# Out[18]: 'acegikmoqs'


# alphabet[::0]
# ValueError: slice step cannot be zero



# equivalent syntax:
# alphabet[12::]
# Out[36]: 'mnopqrst'

# alphabet[12:]
# Out[37]: 'mnopqrst'


# equivalent syntax:
# alphabet[:8:]
# Out[38]: 'abcdefgh'
# alphabet[:8]
# Out[39]: 'abcdefgh'

# equivalent syntax:
# alphabet[:8:2]
# Out[40]: 'aceg'
# alphabet[0:8:2]
# Out[41]: 'aceg'


# \ - back slash
# \n - new string

# TAB: \t
# print("hello\tworld")
# hello	world

#bs = "hello \n world"
#print(bs)

##################################
# Immutability
# name = "Luba"
# name
# Out[58]: 'Luba'
# name[0]
# Out[59]: 'L'
# name[0] = "B"

# TypeError: 'str' object does not support item assignment



# name = "B" + name[1:]
# name
# Out[66]: 'Buba'




###############Concatination of strins +
# "B" + name[1:]
# Out[61]: 'Buba'





##########
# s = "abc"
# s.upper()
    # Out[77]: 'ABC'"ANIDJjnfA".capitalize()
#     #"Adsgfajhd"
#
    #d = '\u1e9e', '\u1e9e'.casefold(), '\u1e9e'.lower()
#a = "A".center(9)
#print(a)
    #'    A    '
#s = 'aaaaKJFAAaakfk'
#c = s.count('aa')
#print(c)
    # 3
#f = "Англиский Russian"
#d = f.encode(encoding = 'koi8_r')
#print(d)
    #b'\xe1\xce\xc7\xcc\xc9\xd3\xcb\xc9\xca Russian'
#d = "ABCDEFG".endswith("FG")
#print(d)
    #True
#s = '0\t1\t22\t333\t4444\t55555\t666666'
#c = s.expandtabs()
#print(c)
    #0       1       22      333     4444    55555   666666
#s = 'GGfdfdGGGGG'
#c = s.find('GG')
#print(c)
    #0
#s = 'карма: {0}, рейтинг: {1}, имя - {name}, ник - {nik_name}'
#с = s.format(711, 1546, name = 'Sam', nik_name = 'SamProfi')
#print(c)
    #'карма: 711, рейтинг: 1546, имя - Sam, ник - SamProfi'
