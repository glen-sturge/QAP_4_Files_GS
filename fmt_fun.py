# $ Format Functions
def f_dol_com_2d(dollar_value):
    # Accepts a numeric value.
    # Returns str of value with '$', comma seperator, 2 decimal places.
    return "${:,.2f}".format(dollar_value)


def f_dol_com_0d(dollar_value):
    # Accepts a numeric value.
    # Returns str of value with '$', comma seperator, truncated at decimal.
    return "${:,.0f}".format(dollar_value)


# Number Format Functions
def f_num_com_2d(value):
    # Accepts a numeric value.
    # Returns str of value with comma seperator, 2 decimal places.
    return "{:,.2f}".format(value)


def f_num_com_0d(value):
    # Accepts a numeric value.
    # Returns str of value with comma seperator, truncated at decimal.
    return "{:,.0f}".format(value)


def f_num_0d(value):
    # Accepts a numeric value.
    # Returns str of value truncated at decimal.
    return "{:.0f}".format(value)


def f_num_1d(value):
    # Accepts a numeric value.
    # Returns str of value truncated at 1 decimal place.
    return "{:.1f}".format(value)


def f_num_2d(value):
    # Accepts a numeric value.
    # Returns str of value truncated at 2 decimal places.
    return "{:.2f}".format(value)


# Date Functions
def f_date_standard(dt_obj):
    # Function will accept dt object
    # Return string in format: yyyy-mm-dd.
    return dt_obj.strftime("%Y-%m-%d")


def f_date_month(dt_obj):
    # Function will accept dt object
    # Return string in format: dd-Mon-yy.
    return dt_obj.strftime("%d-%b-%y")


def f_date_long(dt_obj):
    # Function will accept dt object
    # Return string in format: Day, Month dd, yyyy.
    return dt_obj.strftime("%A, %B %d, %Y")


def f_days_ymwd(days: int):
    # Takes in number of total days.
    # Formats to: ## years, ## months, ## weeks, ## days
    years = 0
    months = 0
    weeks = 0

    if days >= 365:
        years = int(days / 365)
        days = days % 365
    if days >= 30:
        months = int(days / 30)
        days = days % 30
    if days >= 7:
        weeks = int(days / 7)
        days = days % 7
    message = f"{years} years, {months} months, {weeks} weeks, {days} days"
    return message


# Useful Additions.

# | Input Fields of varying character lengths.
def f_inp_f20(prompt: str):
    # Common field to line up input prompts.
    return f"{prompt:<20s}: "


def f_inp_f25(prompt: str):
    # Common field to line up input prompts.
    return f"{prompt:<25s}: "


def f_inp_f30(prompt: str):
    # Common field to line up input prompts.
    return f"{prompt:<30s}: "


def f_inp_f35(prompt: str):
    # Common field to line up input prompts.
    return f"{prompt:<35s}: "


def f_phone_10(number: str):
    # Accepts 10-digit str representing a phone number.
    # Returns formatted: (###) ###-####
    return f"({number[0:3]}) {number[3:6]}-{number[6:]}"


# String Utility Function.
def f_space_cap(user_input: str):
    # Accepts a string.
    # Formats with capital character after each space.
    # Useful in formatting for city names
    # as some with apostrophes (i.e. "St. John's")
    # format incorrectly with .title().
    space_cap = ""
    user_input = user_input.strip().split()
    for index in range(len(user_input)):
        user_input[index] = user_input[index].capitalize()
        space_cap += (user_input[index] + " ")
    space_cap = space_cap.strip()
    return space_cap


def yes_no_dsp(user_input: str):
    # Takes in a string.
    # If it is 'Y', returns 'Yes'.
    # If it is 'N', returns 'No'.
    if user_input == "Y":
        return "Yes"
    elif user_input == "N":
        return "No"
