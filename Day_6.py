def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() != True:

    if front_is_clear() == True and wall_on_right() == True:
        move()
    elif wall_on_right() == False and front_is_clear() == False:
        turn_right()
        move()
    elif wall_on_right() == False and front_is_clear() == True:
        turn_right()
        move()


    else:
        if right_is_clear() == True and wall_in_front() == True:
            turn_right()
        elif wall_on_right() == False or wall_in_front() == True:
            turn_left()

        elif front_is_clear() == True:
            move()
