picture='''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'  ||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-'    o |'|| | ||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'

'''


print('Welcome to game! ;) ')
print('You mast find treasure and steel alive hehe')

first_action=input('Where are you going to? Left or Right???')

if first_action == 'Left':
    second_action = input("What are you going to? Swim in lake or Wait for boat?")

    if second_action=='Wait':
        final_action = input("You see three doors: Red, Yellow and Blue. Go into one of them!")

        if final_action=="Blue":
            print("Cool you did it. I'm really surprised")
            print(picture)
        else:
            print("You are in a fireeee! Bay bitsh")
    else:
        print("You can't swim! You are stupid and you drowned")
else:
    print('Oh no The demon was waiting for you here! So sad... really no(')







