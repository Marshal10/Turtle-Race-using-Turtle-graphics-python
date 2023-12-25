from turtle import *
from random import *
screen=Screen()


colors=["red","green","yellow","blue","violet","orange"]
shuffle(colors)
row=-70
finish_line_reached=False
turtles=[]

def check_pos(turtles):
    for turtle in turtles:
        if turtle.xcor()>=230:    
            winner=turtle.pencolor()
            if user_bet==winner:
                print("Congrats! You won the bet")
            else:
                print(f"You lost the bet.The winner was {winner} turtle")            
            return True   
    return False
    
def random_pace():
    return randint(0,10)
    
def turtle_race(turtle,pace):
    turtle.forward(pace)    

while True:
    user_bet=screen.textinput(title="Make your bet",prompt="Who will win the race? Place your bet").lower()
    if user_bet in ["red","blue","yellow","green","violet"]:
        print("Bet placed successfully")
        break
    else:
        print("Please type in any of the following colors('red','blue','yellow','green','violet')")
screen.setup(width=500,height=400)


for turtle_index in range(0,6):
    turtle=Turtle(shape="turtle")
    turtles.append(turtle)
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230,y=row)
    turtle.speed("fastest")
    row+=30
    
  
while not finish_line_reached:
     
    for turtle in turtles:
        pace=random_pace()
        turtle_race(turtle,pace)   

    finish_line_reached=check_pos(turtles)  
               
screen.exitonclick()