# This function checks whether the sentence
# starts with a capital letter or not.
def starts_with_upper(input_sentence):
    if input_sentence[0].isupper():
        return True
    else:
        return False


# This function checks whether the sentence one of
# the following sentence termination characters: ".", "?", "!".
def ends_with_punct(input_sentence):
    if input_sentence[-1] in ['.', '!', '?']:
        return True
    else:
        return False


# This function checks whether the sentence contains an even amount
# quotation marks. I have added extra validation for cases where
# differently formatted quotations are used
def even_quotations(input_sentence):
    quote_marks = "\""
    amount_of_quote_sets = ((input_sentence.count(quote_marks)
                             + input_sentence.count("“")
                             + input_sentence.count("”")) / 2)
    if amount_of_quote_sets.is_integer():
        return True
    return False


# This function checks whether the sentence contains
# any numbers below 13 that aren't spelt out. It takes
# out any commas so that it will be able to detect
# the numbers.
def number_spelled(input_sentence):
    string_no_commas = ""
    for characters in input_sentence:
        if characters != ",":
            string_no_commas = string_no_commas + characters
    words = string_no_commas.split()
    for word in words:
        if word.isdigit() and int(word) > 0 and int(word) < 13:
            return False
    return True


# This function checks whether the sentence contains
# more than one period.
def period_bar_last(input_sentence):
    num_periods = input_sentence.count(".")
    if input_sentence[-1] == ".":
        num_periods = num_periods - 1
    if num_periods > 0:
        return False
    else:
        return True


# this text explains the program to the user
print("************\tWelcome to my sentence validation program!\t************")
print(" - this program checks the sentence you input for any errors such as:\n"
      "\t - Whether it starts with a capital letter or not.\n"
      "\t - If it has an even number of quotation marks.\n"
      """\t - If your sentence ends with ".", "?" or "!" \n"""
      "\t - That the sentence has no period characters\n\t  "
      " other than the last character.\n"
      """\t - Numbers below 13 are spelled out (”one”, “two”, "three”, etc…)\n""")

while True:

    userInput = input(" - Please enter the sentence you wish to validate below\n - ")

    # Checks if the inputted sentence passes all the checks
    # and lets the user know what checks they did and did'nt pass
    if starts_with_upper(userInput):
        print("Starts with capital letter - PASS")
    else:
        print("Starts with capital letter - FAIL")

    if ends_with_punct(userInput):
        print("""Ends with with ".", "?" or "!" - PASS""")
    else:
        print("""Ends with with ".", "?" or "!" - FAIL""")

    if even_quotations(userInput):
        print("Has an even number of quotation marks - PASS")
    else:
        print("Has an even number of quotation marks - FAIL")

    if number_spelled(userInput):
        print("Numbers below 13 are spelled out - PASS")
    else:
        print("Numbers below 13 are spelled out - FAIL")

    if period_bar_last(userInput):
        print("No period in sentence bar last character - PASS")
    else:
        print("No period in sentence bar last character - FAIL")

    # Asks the user if they want to run the program again
    menuInput = input("\nIf you would like to run this program again please type in \"Y\""
                      "\nIf you would like to exit the program please return any key\n - ")
    if menuInput.lower() == "y":
        print("Running again")
    else:
        break
