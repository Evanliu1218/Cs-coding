def driving(a):
    if a==18 or a>18:
        x="True"
        return x
    else:
        x="False"
        return x

print(driving(16)) #displays False
print(driving(25)) #displays True

def id_triangle(a,b,c):
    if a > b and a > c and b ** 2 + c ** 2 == a ** 2:
        x = 'This is a right angle triangle'
        return x

    if b > a and b > c and a ** 2 + c ** 2 == b ** 2:
        x = 'This is a right angle triangle'
        return x

    if c > b and c > a and b ** 2 + a ** 2 == c ** 2:
        x = 'This is a right angle triangle'
        return x

    if a>b and a>c and a**2<b**2+c**2:
        x="Acute"
        return x
    if c>a and c>b and c**2<a**2+b**2:
        x="Acute"
        return x
    if b>a and b>c and b**2<c**2+a**2:
        x="Acute"
        return x

    elif a>b and a>c and a**2>b**2+c**2:
        x="Obtuse"
        return x
    elif b>c and b>a and b**2>a**2+c**2:
        x="Obtuse"
        return x
    elif c>a and c>b and c**2<b**2+a**2:
        x="Obtuse"
        return x
    else:
        x="It's not a triangle"
        return x
print(id_triangle(3,4,5))

def fizzbuzz(a):
    if a%3==0 and a%5==0:
        x="FIZZ BUZZ!"
        return x
    if a%3==0:
        x="FIZZ!"
        return x
    if a%5==0:
        x="BUZZ!"
        return x
    else:
        x="Huh?"
        return x
print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(7))

import random
x=random.randint(1,6)
y=random.randint(1,6)
z=random.randint(1,6)
count=0
def guess_dice(a,b,c):
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    z = random.randint(1, 6)
    count = 0
    if a==x:
        count+=1
    if b==y:
        count+=1
    if c==z:
        count+=1
    if count==3:
        result="Three correct"
    if count==2:
        result="Two correct"
    if count==1:
        result="One correct"
    if count==0:
        result="Zero correct"
    print("Rolled:", int(x),",", int(y),",", int(z),",",result)
    return result


(guess_dice(5, 3, 1)) #displays: "Rolled: 3, 1, 2, with two correct guesses."
(guess_dice(6, 5, 4)) #displays: "Rolled: 1, 2, 3, with zero correct guesses."

import random
def gimme_random(a,b,c):
    if a=='float':
        y=int(b)
        z=int(c)
        x=random.uniform(y,z)
        return float(x)
    elif a=='int':
        y=int(b)
        z=int(c)
        x=random.randint(y,z)
        return int(x)
print(gimme_random('float', 0.5, 1.9)) #might display 1.2578
print(gimme_random('int', 10, 56)) #might display 22
print(gimme_random('float', 10, 56)) #might display 42.42234
print(gimme_random('int', 0.1, 7.8)) #might display 3
