from turtle import *
from random import randint
speed(10)
penup()
goto(-140, 140)

for step in range(10):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    for dash in range (6):
        forward(10)
        penup()
        forward(10)
        pendown()
    penup()
    backward(130)
    left(90)
    forward(20)

ada = Turtle()
ada.color('orange')
ada.shape('turtle')
ada.penup()
ada.goto(-160, 100)
ada.pendown()
ada.newsteps = 0
ada.name = 'Ada'

bob = Turtle()
bob.color('pink')
bob.shape('turtle')
#bob.resizemode('user')
#bob.shapesize(1, 1, 2)
bob.penup()
bob.goto(-160, 70)
bob.pendown()
bob.newsteps = 0
bob.name = 'Bob'

jam = Turtle()
jam.color('pale turquoise')
jam.shape('turtle')
jam.penup()
jam.goto(-160, 40)
jam.pendown()
jam.newsteps = 0
jam.name = 'Jam'

for turn in range(55):
    adasteps = randint(1,6)
    ada.newsteps = adasteps + ada.newsteps
    ada.forward(adasteps)
    bobsteps = randint(1,6)
    bob.newsteps = bobsteps + bob.newsteps
    bob.forward(bobsteps)
    jamsteps = randint(1,6)
    jam.newsteps = jamsteps + jam.newsteps
    jam.forward(jamsteps)

finalscores = {ada: ada.newsteps, bob: bob.newsteps, jam: jam.newsteps}
winners = [winner for winner, score in finalscores.items() if score == max(finalscores.values())]
for winner in winners:
    print(f'{winner.name} Won!!!')
    for turn in range(10):
        winner.right(36)


#Who wins based off of who crosses the line first
#Take out range and bring in who reached the finish line first based on the new steps
#Have 4 turtle. Each payer get 2 turtle.
#there will be a turtle winner and an overall player winner adding up their 2 tutrles scores