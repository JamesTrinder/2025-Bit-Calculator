# functions go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Main routine goes here
keep_going = ""
while keep_going == "":
    statement_generator("Instructions", "-")
    keep_going = input("Press <enter> to see the instructions or any key to continue")