import turtle
import pandas
#initialaizing the startup screen
screen= turtle.Screen()
screen.bgpic(picname="blank_states_img.gif")
screen.title("U.S State Game")
screen.setup(width=700,height=500)

#reading the data from a file which contains the states and the coordinates .
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
font = ("Arial",10,"normal")


start_text = "guess state"

score = 0
#putting the guessed states to not count them next time
guessed_states = []
while len(guessed_states) < 50:
    #getting input from the user
    guess = screen.textinput(f"Score {score}/50",start_text).capitalize()
    #checking if the user guessed right and did not guess twice.
    if guess in states and guess not in guessed_states:
        turtle.hideturtle()
        turtle.penup()
        #getting
        x = int(data[data.state == guess].x)
        y = int(data[data.state == guess].y)
        turtle.goto(x=x, y=y)
        turtle.write(f"{guess}", False, align="center", font=font)
        score += 1
        guessed_states.append(guess)
        start_text = "What's another state name? "
    #if the user wants to exit the while loop
    elif guess == "Exit":
        break
    else:
        pass

## getting the missed states and printing them in the end
for state in states:
    if state not in guessed_states:
        turtle.hideturtle()
        turtle.penup()
        turtle.color("red")
        x = int(data[data.state == state].x)
        y = int(data[data.state == state].y)
        turtle.goto(x=x, y=y)
        #for putting text on the screen
        turtle.write(f"{state}", False, align="center", font=font)
    else:
        pass













turtle.mainloop()