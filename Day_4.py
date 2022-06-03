

scissors='''

   ____
  / __ |
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  ()  -------  ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/

'''
paper='''

  .--""--.___.._
 (  <__>  )     `-.
 |`--..--'|      <|
 |       :|       /
 |       :|--""-./
 `.__  __;' 
     ""     
'''
rock='''
"!!!ROCK IT, MAN!!!
 !!!GO, MAN, GO!!!"                       _____
        \                              /\| | | |
         \                            / /|_|_|_|
          \                           \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
           /---._.---._.---\        /       /
           \||   '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///||\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/

'''

import random

print("Wellcome to Rock Paper Scissor Game!!!\nChoice 0 for rock, 1 for paper or 2 for scissors")
chose=int(input())

if chose==0:
    print(rock)
elif chose==1:
    print(paper)
else:
    print(scissors)

print("Computer chose:")
rps=[0, 1, 2]
computer_chose=random.choice(rps)

if computer_chose==0:
    print(rock)
elif computer_chose==1:
    print(paper)
else:
    print(scissors)

print("The result:")
if chose==0 and computer_chose==0:
    print("Nobody won!")
elif chose==0 and computer_chose==1:
    print("You are lose!")
elif chose==0 and computer_chose==2:
    print("You are won!")
elif chose==1 and computer_chose==1:
    print("Nobody won!")
elif chose==1 and computer_chose==0:
    print("You are lose!")
elif chose==1 and computer_chose==2:
    print("You are won!")
elif chose==2 and computer_chose==2:
    print("Nobody won!")
elif chose==2 and computer_chose==0:
    print("You are lose!")
elif chose==2 and computer_chose==1:
    print("You are won!")