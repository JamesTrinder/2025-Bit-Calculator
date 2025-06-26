# functions go here
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
- instruction 1
- instruction 2
- etc
    ''')

# Main routine goes here

# Display instructions if wanted
want_instructions = input("Press <enter> to see the instructions "
                          "or any key to continue")

# Continue program if user wants
if want_instructions == "":
    instructions()

print("program continues")