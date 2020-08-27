str1 = 'hello'
str2 = "hello"

str3 = "I don't have a dog"

str4 = "I don't have a dog"

str5 = 'I don"t have a dog'

str6 = 'I don"t have a dog 565465 6546545'


#               'h   e   l   l   o'
# index          0   1   2   3   4
# reverse index  -5  -4  -3  -2 -1

print(str1[4])
print(str1[-1])


# Slicing
# string[start:stop:step]
# including start not including stop!

# for example:
# alphabet[8]
# Out[31]: 'i'
# alphabet[2:8:]
# Out[32]: 'cdefgh'


alphabet = "abcdefghijklmnopqrst"
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

bs = "hello \n world"
print(bs)

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








