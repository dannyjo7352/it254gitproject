#Lab 6a Multiple Shape Sketcher

print("Hello, I am a basic shape sketching tool.")

shape=['square', 'circle', 'rectangle', 'squiggle', 'surprise']

import time

time.sleep(1)

while True:
    
    shape=input("Please choose from one of the pre-selected shapes, and I will draw it for you!" \
    "Or you may type 'quit' at any of the prompts to exit the program. " \
    "You may choose from a square, a circle, rectangle, squiggle, or a surprise:")

    if shape == 'square':
        import turtle
        t=turtle.Pen()
        time.sleep(1)
        print('You have chosen the square.')
        time.sleep(2)
        qty=int(input("How many times would you like me to draw the shape?"))
        time.sleep(1)
        for x in range (0,qty):
            t.up()
            t.left(180)
            t.forward (50)
            t.down()
            t.left(90)
            t.forward(50)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(50)
            t.up()
            t.forward(10)
            t.down()
            t.left(24)

        
    elif shape == 'circle':
        import turtle
        t=turtle.Pen()
        time.sleep(1)
        print('You have chosen the circle.')
        time.sleep(2)
        qty=int(input("How many times would you like me to draw the shape?"))
        time.sleep(1)

        for x in range (0,qty):
            t.up()
            t.right(90)
            t.forward(50)
            t.left(90)
            t.down()
            t.circle(100)
            t.up()
            t.forward(10)
            t.down()
            t.left(7)

        
    elif shape == 'rectangle':
        time.sleep(1)
        import turtle
        t=turtle.Pen()
        print("You have chose the rectangle.")
        time.sleep(2)
        qty=int(input("How many times would you like me to draw the shape?"))
        time.sleep(1)

        for x in range (0,qty):
            t.up()
            t.right(90)
            t.forward(25)
            t.left(90)
            t.down()
            t.forward(50)
            t.left(90)
            t.forward(50)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(50)
            t.left(90)
            t.forward(50)
            t.up()
            t.forward(10)
            t.down()
            t.left(49)

        
    elif shape == 'squiggle':
        time.sleep(1)
        import turtle
        t=turtle.Pen()
        print("You have chosen the squiggle.")
        time.sleep(1)
        qty=int(input("How many times would you like me to draw the shape?"))
        time.sleep(1)
        print("This is a long one.")
        time.sleep(2)
        for x in range(0,qty):
            t.up()
            t.left(180)
            t.forward(200)
            t.left(90)
            t.forward(200)
            t.left(180)
            t.down()
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            time.sleep(5)
            t.up()
            t.forward(10)
            t.down()
            t.left(66)

            print("Please do not ask me to do that again.")

    elif shape == 'surprise':
        time.sleep(1)
        import turtle
        t=turtle.Pen()
        print("You have chosen the surprise. A wise choice.")
        time.sleep(2)
        qty=int(input("How many times would you like me to draw the shape?"))
        time.sleep(1)

        for x in range (0,qty):
            t.up()
            t.back(350)
            t.left(90)
            t.forward(275)
            t.down()
            t.right(180)
            t.forward(300)
            t.left(90)
            t.forward(150)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(220)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(150)
            t.left(180)
            t.up()
            t.forward(500)
            t.left(180)
            t.down()
            t.forward(250)
            t.left(180)
            t.forward(125)
            t.right(90)
            t.forward(270)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(40)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(10)
            t.left(90)
            t.forward(10)
            t.right(90)
            t.forward(30)
            t.up()
            t.forward(10)
            t.down()
            t.left(121)

        
    else:
        time.sleep(2)
        print("Alright, thank you for using the multiple shapes sketcher! Come back soon!")
        break

