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
    myself.speed(10)
    for i in range(1,36):
        drawsquare(myself)
        myself.right(10)
drawart()