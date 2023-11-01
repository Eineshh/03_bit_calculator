# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    # Make string with five character
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():
    statement_generator("Instruction / Information", "=")
    print()
    print("Please choose a data type (image / text / integer)")
    print()
    print("This program assumes that images are being represented in 24 bit color (ie: 24 bits per pixel).  For text, "
          "we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to "
          "quit.")
    print()
    return ""


# Main routine
instructions()
