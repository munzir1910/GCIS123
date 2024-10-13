'''
Baahir's Repository link - https://github.com/Baahir2007/GCIS.git
Hishaam's Repository link - https://github.com/hb7464/hb7464 
Munzir's Repository link - https://github.com/munzir1910/GCIS123 
'''

'''A module containing all the functions required
to draw either from user input or a file'''

'''Intializing the global variables'''
PIXEL_SIZE = 30                     #Length of each pixel side
ycoor = PIXEL_SIZE*10               #The y-coordinate from which pixels start drawing from
xcoor = -PIXEL_SIZE*10              #The x-coordinate from which pixels start drawing from

def get_color(color_string):
        
        """Function takes a number/letter and applies a color to that specific number/letter"""  
        
        if color_string == "0":
            return 'black'
        elif color_string == "1":
            return 'white'
        elif color_string == "2":
            return 'red'
        elif color_string == "3":
            return 'yellow'
        elif color_string == "4":
            return 'orange'
        elif color_string == "5":
            return 'green'
        elif color_string == "6":
            return 'yellowgreen'
        elif color_string == "7":
            return 'sienna'
        elif color_string == "8":
            return 'tan'
        elif color_string == "9":
            return 'gray'
        elif color_string == "A":
            return 'darkgrey'
        else:
            return None

def draw_color_pixel(color_string,turta):
    
    """This function makes one pixel and fills it with a color that has been provided"""
    
    turta.down()
    turta.fillcolor(color_string)
    turta.begin_fill()
    for i in range(4):
        turta.forward(PIXEL_SIZE)
        turta.right(90)
    turta.forward(PIXEL_SIZE)
    turta.end_fill()

def draw_pixel(color_string_number,turta):
    
    """This function makes one pixel and fills it with a color that has been provided"""
    
    color_string = get_color(color_string_number)
    draw_color_pixel(color_string, turta)

def draw_line_from_string(color_string_line, turta):  

    '''A function that takes a string of characters and 
    draws a line using the draw_pixel function in a loop'''
    
    try:

        for i in color_string_line:    
            draw_pixel(i,turta)
    
    except:
    
        return False

def draw_shape_from_string(turta):

    """ A function that prompts a color string 
        from the user under a loop until the user 
        enters an empty string or if that color is 
        not defined and it is the initial step for 
        drawing the colored pixel """
    
    y = 0
    while True:
        Row_Color = input("Enter a color string: ").strip()
        turta.penup()
        turta.goto(xcoor, ycoor - y)
        turta.pendown()
        turta.speed(0)
        Rows = draw_line_from_string (Row_Color, turta)
        if Row_Color == "" or Rows == False:
            break
        else:
            y += PIXEL_SIZE
        
def draw_grid(turta):
    
    """A function that draws a 
       20x20 color grid"""

    Color1 = input("Enter color1: ")
    Color2 = input("Enter color2: ")
    String1 = (Color1 + Color2)*10
    String2 = (Color2 + Color1)*10
    row = 0
    while row < 10:
        y = 0
        for i in range(10):
            turta.penup()
            turta.goto(xcoor,ycoor - y)
            turta.pendown()
            draw_line_from_string (String1, turta)
            y += PIXEL_SIZE
            turta.penup()
            turta.goto(xcoor,ycoor - y)
            turta.pendown()
            draw_line_from_string (String2, turta)
            y += PIXEL_SIZE
            row += 1
                        
def draw_shape_from_file(turta):
    
    '''A function designed to take a file path 
    from the user that contains characters that 
    correlate to colors as listed in the get_colour
    function and reads the file line by line feeding
    it into the draw_line_from_string function to 
    create a full image'''
    
    filepath = input("Enter a file path: ")
    with open(filepath) as file:
        
        Row=0
        
        for line in file:

            turta.up()
            turta.goto(xcoor,ycoor-(PIXEL_SIZE*Row))
            draw_line_from_string(line, turta)
            Row += 1
