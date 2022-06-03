import random

letters=['A', 'a', 'B', 'b', 'C', 'c']
numbers=['1', '2', '3', '4', '5', '6', '7']
symbols=['!', '@', '#', '$', '%']

print('Wellcome to the Password Generator!;0 ')
nr_letters=int(input("How many letters: "))
nr_numbers=int(input('How many numbers: '))
nr_symbols=int(input('How many symbols: '))
#
# password=''
# for letter in range(1, nr_letters+1):
#     ro_lett = random.choice(letters)
#     password=password+ro_lett
# for number in range(1, nr_numbers+1):
#     ro_numb=random.choice(numbers)
#     password=password+ro_numb
# for symbol in range(1, nr_symbols+1):
#     ro_symb=random.choice(symbols)
#     password=password+ro_symb
#
# print(password)



# or just
# for letter in range(1, nr_letters+1):
#   password+=randome.choise(letters)

# next level
password_list=[]

for sraka in range(1, nr_letters+1):
    password_list.append(random.choice(letters))
for srak in range(1, nr_numbers +1):
    password_list.append(random.choice(numbers))
for sra in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))

# for characters in password_list:
num_list=len(password_list)
new_password_list=random.choices(password_list, k=num_list)
# shuffle(List) команда що також поже перемішувати
print(''.join(new_password_list))

# for characters in password_list:
#     print(characters)

