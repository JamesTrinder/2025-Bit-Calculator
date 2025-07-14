# Ask a user for width and loop until they
# give an answer that is more than zero
def int_check(question, low):

    error = f"Please enter a number that is more than or equal to {low}\n"
    while True:

        try:
            #ask the user for an input
            response = int(input(question))

            #check the number is more than zero
            if response >= low:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# calculates how many bits are needed to represent an image
def image_calc():
    # Get the image dimensions
    width = int_check(question="Width: ", low=1)
    height = int_check(question="Height: ", low=1)

    # calculate the number of pixels and multiply by 24 to get the number of bits
    num_pixels = width * height
    num_bits = num_pixels * 24

    # Set up answer and return it
    answer = (f"Number of pixels:  {width} x {height} = {num_pixels}"
              f"\nNumber of bits: {num_pixels} x 24 = {num_bits}")

    return answer


# Main routine goes here
image_ans = image_calc()
print(image_ans)