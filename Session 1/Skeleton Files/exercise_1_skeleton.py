"""Exercise 1: Take a list of coordinates (list of tuples), and find the smallest x value (first value of tuple)

Remember to fill out all the TODO's, you can quickly scan for them by pressing CTRL/CMD + F
"""

coordinates = [(1, 2), (2, 3), (4, 5), (6, 7)] # Setup the list of coordinates

# Pick initial 
lowest_x_coord = ... # TODO: Fill out an initial value

for coordinate_pair in coordinates: # Go through each pair
    ... # TODO: fill out what check needs to happen here

print(lowest_x_coord == 1) # Should print True if you are right
