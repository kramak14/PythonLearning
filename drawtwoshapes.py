import turtle

def drawsquare():
    window = turtle.Screen()
    window.bgcolor("blue")  #Sets window color to be blue

    myself = turtle.Turtle()
    myself.shape("turtle") #Sets the shape as a turtle
    myself.color("orange") #Sets turtle color as orange
    myself.speed(1)

    myself.forward(100) #Moves forward a distance
    myself.right(90)    #Moves right by 90 degrees
    myself.forward(100)
    myself.right(90)
    myself.forward(100)
    myself.right(90)
    myself.forward(100)
    myself.right(90)

    #Instantiates a new turtle to draw a new shape after first shape
    #drawn is done.
    lima = turtle.Turtle()
    lima.shape("arrow")  # Sets new shape as a turtle
    lima.color("magenta")  # Sets new color as magenta
    lima.circle(100)

    window.exitonclick()

drawsquare()