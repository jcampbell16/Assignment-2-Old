# Jasmine Campbell 250886086
from math import pi


def cube_volume():  # Define cube volume
    side_length = int(input('Please enter the side length: '))
    c_volume = side_length ** 3  # Cube volume equation
    c_volume = ("%.2f" % c_volume)  # Convert two decimal places
    print('The volume of a cube with a side length of {} is {}.'.format(side_length, c_volume))
    return c_volume


def pyra_volume():  # Define pyramid volume
    base_length = int(input('Please enter base length:'))
    height = int(input('Please enter height:'))
    p_volume = (1/3*((base_length ** 2)*height))  # Pyramid volume equation
    p_volume = ("%.2f" % p_volume)  # Convert two decimal places
    print('The volume of a pyramid with a base of {} and height of {} is {}.'.format(base_length, height, p_volume))
    return p_volume


def elli_volume():  # Define ellipsoid volume
    rad_one = int(input('Please enter the first radius:'))
    rad_two = int(input('Please enter the second radius:'))
    rad_three = int(input('Please enter the third radius:'))
    e_volume = ((4/3*pi)*rad_one*rad_two*rad_three)  # Ellipsoid volume equation
    e_volume = ("%.2f" % e_volume)  # Convert two decimal places
    print('The volume of a ellipsoid with a radius of {}, {}, {} is {}'.format(rad_one, rad_two, rad_three, e_volume))
    return e_volume
# Start lists blank and shape empty
c_list = []
p_list = []
e_list = []
shape = ""

# Start Loop

while shape != 'quit':  # Make sure to check input
    shape = input('Please choose a shape (cube, pyramid, ellipsoid) or type \'quit\' to end: ').lower()
    if shape == 'cube':
        cube_result = cube_volume()
        c_list.append(cube_result)
        # Figure out how to save values within a loop (lists)
    elif shape == 'pyramid':
            p_result = pyra_volume()
            p_list.append(p_result)
    elif shape == 'ellipsoid':
            r_result = elli_volume()
            e_list.append(r_result)

# Format to look pretty
c1 = ", ".join(map(str, c_list))
p1 = ", ".join(map(str, p_list))
e1 = ", ".join(map(str, e_list))

# Check to see if there was input
if len(c_list) == 0 and len(p_list) == 0 and len(e_list) == 0:
    print('You have come to the end of your session. \nYou did not perform any calculations.')
else:
    print('You have come to the end of your session.\nThe volumes for each shape are calculated below:')
    print('Cube: {} \nPyramid: {} \nEllipsoid: {}'.format(c1, p1, e1))
