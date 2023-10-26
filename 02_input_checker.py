# checks user choice is 'integer', 'text' or 'image'
def user_choice():

    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()

        # If they choose "t" or "text", return "text"
        if response == "text" or response == "t":
            return "text"

        else:
            # if response is not valid, output an error
            print("Please choose a valid file type!")
            print()


# Main routine goes here
data_type = user_choice()
print("You chose", data_type)

print()