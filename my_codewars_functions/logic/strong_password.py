import re
def check_password(s):
    """

    Your users passwords were all stole in the Yahoo! hack,
    and it turns out they have been lax in creating secure passwords.
    Create a function that checks their new password (passed as a string)
    to make sure it meets the following requirements:
    Between 8 - 20 characters
    Contains only the following characters: (and at least one character from each category):
    uppercase letters, lowercase letters, digits, and the special characters !@#$%^&*?
    Return "valid" if passed or else "not valid

    """
    letters = re.sub("[^a-zA-Z]+", "", s)
    digits = re.sub("[^0-9]", "", s)
    special_characters =  [i for i in s if i in "!@#$%^&*?"]
    only_characters = re.sub("[^A-Za-z\d!@#$%^&*?]+","",s)
    if (letters != letters.lower()) and (letters!= letters.upper()) and (len(letters) >= 2) and len(digits)>0 and len(special_characters)>0 and 8<= len(s) <=20 and s == only_characters:
        return 'valid'
    else:
        return "not valid"
if __name__ == '__main__':
    pass
    res = check_password(s='Paaaaaa222!!!')
    print(res)