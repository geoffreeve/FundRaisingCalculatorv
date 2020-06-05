# Not blank function
def not_blank(question, error_msg, num_check):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        # If num_check == yes then check for numbers
        if num_check == "yes":
            # If num in response then print error
            for letter in response:
                if letter.isdigit():
                    has_errors = "yes"
                    break
        # Else check for letters
        else:
            for letter in response:
                if not letter.isdigit():
                    has_errors = "yes"
                    break
        # If response is blank, print error
        if response == "":
            print(error)
            continue
        # If has error is not blank, print error
        elif has_errors != "":
            print(error)
            continue
        # If everything is good then return response
        else:

            return response


# Main routine
item = not_blank("What are you selling? ",
                 "Your response cannot have numbers or be blank",
                 "yes")
sold = not_blank("How many are you selling? ",
                 "Your response cannot contain text or be blank",
                 "no")

print("You are selling {} {}".format(sold, item))
