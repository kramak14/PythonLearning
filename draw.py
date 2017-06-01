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

    window.exitonclick()

drawsquare()