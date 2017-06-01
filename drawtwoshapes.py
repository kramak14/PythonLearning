import turtle

def drawsquare(aTurtle):
    for i in range(1,5):
        aTurtle.forward(100) #Moves forward a distance of 100.
        aTurtle.right(90) #Moves right a distance of 90 degrees

def drawart():
    window = turtle.Screen()
    window.bgcolor("blue")  #Sets window color to be blue

    #Create a turtle instance
    myself = turtle.Turtle()
    myself.shape("turtle") #Sets the shape as a turtle
    myself.color("orange") #Sets turtle color as orange
    myself.speed(1)
    drawsquare(myself)

    # Instantiates a new turtle to draw a new shape after first shape
    # drawn is done.
    lima = turtle.Turtle()
    lima.shape("arrow")  # Sets new shape as a turtle
    lima.color("magenta")  # Sets new color as magenta
    lima.circle(100)



    window.exitonclick()

drawart()