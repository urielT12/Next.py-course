import string


class UsernameContainsIllegalCharacter(Exception):
    """exception for times that username contains a char that is not an uppercase ,a lowercase, a number or
    an underscore"""
    def __init__(self,char,index):
        self._char = char
        self._index = index

    def __str__(self):
        return f"Username contains an Illegal Character '{self._char}' at index {self._index}"

class UsernameTooShort(Exception):
    """exception for times that username is under 3 chars long"""
    def __init__(self,arg):
        self._arg = arg

    def __str__(self):
        return "Username too short"

class UsernameTooLong(Exception):
    """exception for times that username is more than 16 chars long"""
    def __init__(self,arg):
        self._arg = arg

    def __str__(self):
        return "Username too long"

class PasswordMissingCharacter(Exception):
    """exception for times that the password not contains at least - one uppercase , one lowercase
     ,one number and one string.punctuation"""
    def __init__(self,arg):
        self._arg = arg

    def __str__(self):
        return "Password Missing Character"


class PasswordMissingUppercase(PasswordMissingCharacter):
    """exception for times that password missing uppercase, expand PasswordMissingCharacter exception"""
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return super().__str__() + " (Uppercase)"

class PasswordMissingLowercase(PasswordMissingCharacter):
    """exception for times that password missing lowercase, expand PasswordMissingCharacter exception"""
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return super().__str__() + " (Lowercase)"

class PasswordMissingDigit(PasswordMissingCharacter):
    """exception for times that password missing digit, expand PasswordMissingCharacter exception"""
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return super().__str__() + " (Digit)"

class PasswordMissingSpecial(PasswordMissingCharacter):
    """exception for times that password missing special character, expand PasswordMissingCharacter exception"""
    def __init__(self, arg):
        self._arg = arg

    def __str__(self):
        return super().__str__() + " (Special)"

class PasswordTooShort(Exception):
    """exception for times that the password is under 8 chars long"""
    def __init__(self,arg):
        self._arg = arg

    def __str__(self):
        return "Password too short"

class PasswordTooLong(Exception):
    """exception for times that the password is longer than 40 chars"""
    def __init__(self,arg):
        self._arg = arg

    def __str__(self):
        return "Password too long"

def pass_check(password):
    """a function that I add for convenience, returns for a password which char is it missing"""
    upper = False
    lower = False
    number = False
    punctuation = False
    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            number = True
        elif char in string.punctuation:
            punctuation = True
    if not upper:
        return "upper"
    elif not lower:
        return "lower"
    elif not number:
        return "number"
    elif not punctuation:
        return "punctuation"

def check_input(username, password):
    """receives two parameters of type string: username and password. The function prints "OK" if the username and password are correct,
        If the username or password (or both) do not meet the defined conditions - throw the suitable exception"""
    try:
        if len(username) < 3:
            raise UsernameTooShort(len(username))
        if len(username) > 16:
            raise UsernameTooLong(len(username))
        if len(password) < 8:
            raise PasswordTooShort(len(password))
        if len(password) > 40:
            raise PasswordTooLong(len(password))
        badlist = [char for char in range(len(username)) if not username[char].isalpha() and username[char] not in "123456789_"]
        if len(badlist) != 0:
            raise UsernameContainsIllegalCharacter(username[badlist[0]],badlist[0])
        if pass_check(password) == "upper":
            raise PasswordMissingUppercase(len(password))
        if pass_check(password) == "lower":
            raise PasswordMissingLowercase(len(password))
        if pass_check(password) == "number":
            raise PasswordMissingDigit(len(password))
        if pass_check(password) == "punctuation":
            raise PasswordMissingSpecial(len(password))
        print("OK")
    except (UsernameContainsIllegalCharacter, UsernameTooShort, UsernameTooLong,
            PasswordMissingCharacter, PasswordTooShort, PasswordTooLong) as e:
        print(e)




def main():
    """3."""
    print("3.")
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")
    """4."""
    print("4.")
    username = input("please enter your username: ")
    password = input("please enter your password: ")
    check_input(username,password)
    """5. 1."""
    print("5.1.")
    check_input("A_a1.", "12345678")
    """5. 2."""
    print("5.2.")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")


if __name__ == "__main__":
    main()