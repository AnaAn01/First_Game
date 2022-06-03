import random

word_list=['ardvark', 'baboon', 'camel']

chosen_word=random.choice(word_list)

print(chosen_word)

display=[]
for latter_display in chosen_word:
    display.append('_')
print(display)

guess=input('Choice a latter: ').lower()


for position in range(len(chosen_word)):
    latter=chosen_word[position]
    if guess==latter:
        display[position]=latter

print(display)


# for latter in chosen_word:
#     if guess==latter:
#         print('Right')
#     else:
#         print('Wrong')