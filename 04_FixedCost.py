import time


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

        # If response is blank, print error
        if response == "":
            print(error)
            continue
        # If not checking for numbers then check if its lower or equals 0
        try:
            if num_check == "no" and float(response) <= 0:
                print("Please enter a number higher than 0.")
                continue
        except ValueError:
            print("Please enter a number")
            continue

        # If has error is not blank, print error
        if has_errors != "":
            print(error)
            continue
        # If everything is good then return response
        else:
            return response


# Num total function
def num_total(amount, price, printing, packaging):
    advertise = 20
    stall = 20
    # Using int/float() to convert str to int/float
    # Amount reduced from printing
    reduced = float(printing) * int(amount) + float(packaging) * int(amount)
    # Total variable cost
    varCost = float(price) * int(amount) - reduced
    varCost -= advertise + stall

    # Returns total variable cost
    return varCost


# Main routine
# Getting variables with not_blank function
valid = False
while not valid:
    item = not_blank("What are you selling? ",
                     "Your response cannot have numbers or be blank",
                     "yes")
    amount = not_blank("How many are you selling? ",
                       "Your response cannot contain text or be blank",
                       "no")
    price = not_blank("How much are you selling for? ",
                      "your response cannot contain text or be blank",
                      "no")
    printing = not_blank("How much will printing be per item? ",
                         "Your response cannot contain text or be blank",
                         "no")
    packaging = not_blank("How much will packaging be per item? ",
                          "Your response cannot contain text or be blank",
                          "no")

    # Using the acquired variables to get total cost
    total = num_total(amount, price, printing, packaging)

    # Showing calculations
    print(
        "\nSelling details:\nSelling: {}\nStock: {}\nPrice: ${}\n\nFixed Costs:\nAdvertising: ${}\nStalls: ${}\n\nTotal - "
        "Packaging/Printing and Advertising/Stalls =\n${} Profit".format(item,
                                                                        amount, price,
                                                                        20, 50,
                                                                        total))

    # Ask user if they want to restart or exit
    cont = not_blank("\nEnter any number to continue, or type 55 to stop. ", "Please enter a number.", "no")
    # If user enters 1 then continue
    if float(cont) == 55:
        break
    # Otherwise break to stop program
    else:
        continue
