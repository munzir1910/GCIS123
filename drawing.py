'''A module designed to execute all 
the relevant functions from the pixart module'''

import turtle
import pixart as pa

def main():
    
    '''The main function that 
    contains the relevant functions'''

    color = input("Enter a color number: ")
    pa.draw_pixel(color)

    pa.draw_shape_from_string(turtle)
    input("Do you want to continue? ")
    
    pa.draw_grid()
    input("Do you want to continue? ")

    pa.draw_shape_from_file(turtle)
    input("Press enter to close the program")

if __name__ == '__main__':
    main()