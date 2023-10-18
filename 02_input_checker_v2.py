# checks user choice is 'integer', 'text' or 'image'
def user_choice():
    # Lists of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "p", "pic"]

    valid = False
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()

        # Checks for valid response and returns text, integer, or image

        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for an image")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            # if response is not valid, output an error
            print("Please choose a valid file type!")
            print()


# Main routine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)
    print()
