def both():
    counter=1
    while counter < 3:
        counter += 1
        for x in range(8, -4, -1):
            print (x)

both()

def is_odd():
    for x in range (1, 11):
        num = x % 2
        if num == 0:
            print(x, "is even")
        else:
            print(x, "is odd")

is_odd()

import random
def  dice_roll(a):
    counter = 0
    num = 0
    while num != a:
        counter += 1
        x = random.randint(0, 6)
        y = random.randint(0, 6)
        z = random.randint(0, 6)
        num = x + y + z
    return counter

print(dice_roll(17))

def odd_even_count(a):
    even = 0
    odd = 0
    while a > 0:
        num = a % 10
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        a = int(a/10)
    x = "Even:" + str(even) +  " Odd:" + str(odd)
    return x

print(odd_even_count(5234))

def string_analysis(word):
    blanks = 0
    let = 0
    dig = 0
    for letter in word:
        if letter == " ":
            blanks += 1
        elif letter.isalpha() == True:
            let += 1
        elif letter.isdigit() == True:
            dig +=1
    x = "Letters:" + str(let) + " Digits:" + str(dig) + " Blanks:" + str(blanks)
    return x
print(string_analysis("I'm not 89 years old"))
