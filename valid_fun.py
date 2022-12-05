def not_blank(user_input: str):
    # Accepts str
    # Returns False if blank, otherwise True.
    if user_input.strip() == "":
        print("Cannot Be Blank.")
        return False
    else:
        return True


def check_postal(user_input: str):
    # Accepts str
    # Returns False if not in format of 'L#L#L#', otherwise True.
    if len(user_input) == 6 and\
            user_input[0].isalpha() and user_input[2].isalpha() and user_input[4].isalpha() and\
            user_input[1].isdigit() and user_input[3].isdigit() and user_input[5].isdigit():
        return True
    else:
        print("Not A Valid Postal Code.")
        return False


def check_phone(user_input: str):
    # Accepts Str
    # Returns True if format is '###-###-####', otherwise False.
    if (user_input[3] and
            user_input[7]) == '-' and len(user_input.replace('-', '')) == 10 and user_input.replace('-', '').isdigit():
        return True
    else:
        print("Check Input. Try Again")
        return False


def check_yes(user_input: str):
    # Takes in Str.
    # If Str is 'Y', returns True.
    # If Str is 'N', returns False.
    if user_input == 'Y':
        return True
    elif user_input == 'N':
        return False
