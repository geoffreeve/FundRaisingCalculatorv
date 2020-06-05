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
        if num_check == "no" and float(response) <= 0:
            print("Please enter a number higher than 0.")
            continue
        # If has error is not blank, print error
        elif has_errors != "":
            print(error)
            continue
        # If everything is good then return response
        else:
            return response


# Pause function
def pause():
    time.sleep(.50)


# Num total function
def num_total(amount, price, printing, packaging):
    # Using int/float() to convert str to int/float
    # Amount reduced from printing
    Reduced = float(printing) * int(amount) + float(packaging) * int(amount)
    # Total variable cost
    varCost = int(price) * int(amount) - Reduced

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

    # Printing costs
    pause()
    print("--Variable costs--\nPrinting : {} x {} = {}".format(printing, amount, float(printing) * int(amount)))
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
    # Packaging costs
    pause()
    print("Packaging : {} x {} = {}".format(packaging, amount, float(packaging) * int(amount)))
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
    # Showing calculations
    pause()
    print("Total costs:\nSelling: {}\nStock: {}\nPrice: {}\nProfit: {}\nProfit - Packaging and Printing =\n {}".format(item, amount,
                                                                                                        price, total + float(packaging) + float(printing),
                                                                                                        total))
    # Printing total
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
    pause()
    print("You are selling {} {}'s for ${}".format(amount, item, total))
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")

    # Ask user if they want to restart or exit
    cont = not_blank("Go again? 1) Yes 2) No", "Enter 1 or 2", "no")
    # If user enters 1 then continue
    if int(cont) == 1:
        continue
    # Otherwise break to stop program
    else:
        break
