import turtle
import pandas as pd

screen = turtle.Screen()

screen.title('U.S States Game')
image = 'blank_states_img.gif'      # path

screen.addshape(image)           # Add this GIF file as a possible turtle shape. Loaded to screen
turtle.shape(image)              # turtle object can be an image also

states_file = open('50_states.csv')
states_df = pd.read_csv(states_file)
states_list = list(states_df['state'])
# print(states_df)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt="What's another state's name?").title() # type: ignore  
    """
# print(answer_state)
# print(type(answer_state))


# correct_row = states_df[states_df['state'] == answer_state]
# # print(correct_row)
# x_coordinate = float(correct_row.iloc[0]['x'])

# # print(type(x_coordinate))       #<class 'pandas.core.series.Series'>
# # print(x_coordinate)
# y_coordinate = float(correct_row.iloc[0]['y'])  """
             #either use 'state' as a key (like we used) or as attribute

    if answer_state == 'Exit':
    # Showing list of correctly guesses states in new file
        missing_states = [state for state in states_list if state not in guessed_states]
        # print(missing_states)
        missing_data = pd.DataFrame(missing_states)
        missing_data.to_csv('states_to_learn.csv')
        break

    else:
        name_object = turtle.Turtle()
        name_object.hideturtle()
        name_object.penup()
        correct_row = states_df[states_df['state'] == answer_state]
        name_object.goto(correct_row.x.item(), correct_row.y.item())
        name_object.write(answer_state)
        guessed_states.append(answer_state)

                    
def get_mouse_click_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_mouse_click_coor)      #event listener

# turtle.mainloop()      #keeps screen open even though the code has finished running, otherwise screen just flashes and disappear

# note that here we didnt use screen.exitonclick()