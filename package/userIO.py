# stores the contents of file in a string and returns it
def loadTextFile(name):
    lines = ""
    for f in open('resources/' + name + '.txt'):
        lines += f
    return lines

def validatePassword(password):
    SpecialSymbol = ['$', '@', '#', '%', '!', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '`', '~', '[', '{', ']',
                     '}', '|', ';', ':', ',', '<', '.', '>', '/', '?']
    val = True

    # if password is too short
    if len(password) < 8:
        print('Your password needs to have 8 characters at least!')
        val = False
    # if password is too long
    if len(password) > 20:
        print('Your password can not exceed 12 characters!')
        val = False
    # if password doesn't contain digits
    if not any(char.isdigit() for char in password):
        print('Your password needs to contains at lease one digit!')
        val = False
    # if password doesn't contain uppercase char
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False
    # if password doesn't contain lowercase char
    if not any(char.islower() for char in password):
        print('Your password needs to contains at lease one capital character!')
        val = False
    # if password doesn't contain special char
    if not any(char in SpecialSymbol for char in password):
        print('Your password need to contain at least one non-alpha character!')
        val = False

    return val


# function name is its functionality 
def capitalize_First_Letter_Of_Every_Word(str):
    word_list = str.split()
    new_str =""
    for x in word_list:
        new_str = new_str + x.capitalize() + " "
    return new_str