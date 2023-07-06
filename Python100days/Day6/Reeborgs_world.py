# Here's my official short program for Hurdle and Maze in Reeborg's 
# world on reeborg.ca. It runs only on the Reeborg python compiler 
# online if you wish to give it a try

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear(): # This part solves an infinte loop case if it meets one
    move()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        turn_left()
    else:
        move()

# at_goal() is an inbuilt funct that marks the ending point in each game
# right_is_clear() func checks if there's no wall on the robots right
# wall_in_front() func checks if there's a wall facing the robot
# the move() func permits the robot to go one step ahead
# turn_left() is an inbuilt func for movx to the left
# turn_right() is a defined func that permits us to turn_right = turn_left * 3