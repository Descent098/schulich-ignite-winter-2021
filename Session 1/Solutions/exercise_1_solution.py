"""Exercise 1 Solution: Take a list of coordinates (list of tuples), and find the smallest x value (first value of tuple)

Steps:
    1. First we picked a starting number from the list (the first x value of the tuples)
    2. Then on the iteration we check if the current value is greater than the current itteration's x value
    3. If the current itteration's x value is smaller, then assign it to the lowest_x_coord variable, else just continue the loop
    4. Print the lowest coordinate at the end
"""

coordinates = [(1, 2), (2, 3), (4, 5), (6, 7)] # Setup the list of coordinates

# Pick initial number (Note we could have also just picked a REALLY big number here instead)
lowest_x_coord = coordinates[0][0] # x value of the first pair

for coordinate_pair in coordinates: # Go through each pair
    if lowest_x_coord > coordinate_pair[0]: # If current lowest x is larger than current coordinate pair x value
        lowest_x_coord = coordinate_pair[0]

print(lowest_x_coord)
