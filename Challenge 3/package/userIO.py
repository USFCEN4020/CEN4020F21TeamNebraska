from package import dbWrite as wr

def loadTextFile(name):
    lines = ""
    for f in open('resources/' + name + '.txt'):
        lines += f
    return lines

def validatePassword(password):
    SpecialSymbol = ['$', '@', '#', '%', '!', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '`', '~', '[', '{', ']',
                     '}', '|', ';', ':', ',', '<', '.', '>', '/', '?']
    val = True

    if len(password) < 8:
        print('Your password needs to have 8 characters at least!')
        val = False

    if len(password) > 20:
        print('Your password can not exceed 12 characters!')
        val = False

    if not any(char.isdigit() for char in password):
        print('Your password needs to contains at lease one digit!')
        val = False

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in password):
        print('Your password needs to contains at lease one capital character!')
        val = False

    if not any(char in SpecialSymbol for char in password):
        print('Your password need to contain at least one non-alpha character!')
        val = False

    return val

def postJob(db, userName):
    print("\nEnter 'cancel' at any time to cancel.\n")
    title = input("Enter job title: ")
    if(title=='cancel'):
        print("Returning to main menu.")
        return
    description = input("Enter job description: ")
    if(description=='cancel'):
        print("Returning to main menu.")
        return
    employer = input("Enter job employer: ")
    if(employer=='cancel'):
        print("Returning to main menu.")
        return
    location = input("Enter job location: ")
    if(location=='cancel'):
        print("Returning to main menu.")
        return
    salary = input("Enter job salary (in USD please): ")
    if(salary=='cancel'):
        print("Returning to main menu.")
        return
    wr.commitJob(userName, db, title, description, employer, location, salary)