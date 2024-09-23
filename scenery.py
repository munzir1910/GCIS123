import turtle as t

# Customizatons:
screen = t.Screen()
screen.setup(width=600, height=600)
t.bgcolor("skyblue") # this is to make the background color skyblue
t.speed(0) # this is so the drawing gets completed quickly

def table(tw,tc): # this is a function for the table top
    t.fillcolor(tc)
    t.begin_fill()
    t.forward(tw//2) # we are dividing by 2 so we can draw the right top side of the table
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(tw)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(tw//2) # we are dividing by 2 so we can draw the left top side of the table
    t.end_fill()

def tablelegs(tw,tll,tlc):
    t.penup()
    t.goto(tw//2,-10) # we are dividing by 2 so we can go to the bottom right corner of the table
    t.fillcolor(tlc)
    t.begin_fill()
    t.pendown()
    t.setheading(270)
    t.forward(tll)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(tll)
    t.end_fill()

def cakedetails(): # here we are asking the user for their preferences so they can customize their cake
    cw = float(input("Enter a width for the layers (less than table width): "))
    ch1 = float(input("Enter 1st layer height: "))
    cc1 = input("Enter 1st layer color: ")
    ch2 = float(input("Enter 2nd layer height: "))
    cc2 = input("Enter 2nd layer color: ")
    ch3 = float(input("Enter 3rd layer height: "))
    cc3 = input("Enter 3rd layer color: ")
    return cw,ch1,ch2,ch3,cc1,cc2,cc3 # here we are returning the variables so we can use them later
    
def cakelayers(cw,ch,cc,height): # here is how each cake layer is created
    t.penup()
    t.goto(-cw//2,height) # we are making it negative and dividing by two to allow the cake layers to be centered on the table
    t.fillcolor(cc)
    t.begin_fill()
    t.pendown()
    t.forward(ch)
    t.right(90)
    t.forward(cw)
    t.right(90)
    t.forward(ch)
    t.right(90)
    t.right(90)
    t.end_fill()
    
def decoration1(cw,height): # this makes four white semi-circles on the top layer for decoration
    t.penup()
    t.goto(-cw//2,height) 
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    t.setheading(270)
    t.circle(cw/8,180) # we are dividing by 8 so each semi-circle fits with the width of the cake
    t.setheading(270)
    t.circle(cw/8,180)
    t.setheading(270)
    t.circle(cw/8,180)
    t.setheading(270)
    t.circle(cw/8,180)
    t.end_fill()

def decoration2(height): # this makes a red ball on top of the cake in the middle
    t.penup()
    t.goto(10,height)
    t.fillcolor("red")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def main():

    tw = float(input("Enter the width of the table: ")) # asking the user for their preferences
    tc = input("Enter the color of the table: ") # asking the user for their preferences
    table(tw,tc)

    tll = float(input("Enter the length of the legs: ")) # asking the user for their preferences
    tlc = input("Enter the color of the legs: ") # asking the user for their preferences
    tablelegs(tw,tll,tlc)
    tablelegs(tw//2,tll,tlc)
    tablelegs(-tw//2 + 20,tll,tlc)
    tablelegs(-tw + 20,tll,tlc)

    cw,ch1,ch2,ch3,cc1,cc2,cc3 = cakedetails() # this is were the return function is being used for 
    
    if cw > tw: # here if the cake width is larger than the table width it will print that and turtle will crash
        print("Cake is too big!!")
        return
    else:
        print("Preparing Cake!!") # if it isnt it will print this and continue with the rest of the code
        
        height = 0  # this is so the cake can start on top of the table top
        cakelayers(cw,ch1,cc1,height)
        height += ch1 # this is to assign a new value to the same variable
        
        cakelayers(cw,ch2,cc2,height)
        height += ch2
        
        cakelayers(cw,ch3,cc3,height)
        height += ch3
        
        decoration1(cw,height)
        height += 10
        
        decoration2(height)

        print("Happy Birthday!!")
    
    input("Enter to exit... ") # the user can exit whenever they want

main()