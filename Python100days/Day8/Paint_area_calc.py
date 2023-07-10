
import math
# Define a function called paint_calc() so that the code below works. 
def paint_calc(height, width, cover):
    num_of_cans = math.ceil((height*width)/cover)  #the ceil() func returns the smallest integer >= x.
    print(f"You'll need {num_of_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)