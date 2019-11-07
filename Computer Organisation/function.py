import cmath
def mixed_number(a,b):
    whole_number=a//b
    numerator=a%b
    return str(whole_number)+ " "+str(numerator)+ "/"+ str(b)
print(mixed_number(9,2))

def vowel_count_1(a):
    x = a.count('a')
    x += a.count('e')
    x += a.count('i')
    x += a.count('o')
    x += a.count('u')
    return x
print(vowel_count_1('This is a sample'))

def vowel_count_2(a):
    x = a.count('a')
    x1 = a.count('e')
    x2 = a.count('i')
    x3 = a.count('o')
    x4 = a.count('u')
    return str(x)+","+str(x1)+","+str(x2)+","+str(x3)+","+str(x4)
print(vowel_count_2('This is a sample'))

def sphere_volume(r):
    x= 4/3*(cmath.pi)*r**3
    return x
print(int(sphere_volume(10)))

def sphere_surface_area(r):
    x= 4*(cmath.pi)*r**2
    return x
print(int(sphere_surface_area(10)))

def sphere_metrics(r):
    x = 4 / 3 * (cmath.pi) * r ** 3
    y = 4 * (cmath.pi) * r ** 2
    return "Sphere Volume:"+str(x) +"Sphere Surface Area:"+ str(y)
print(sphere_metrics(10))

def name_function(a,b,c):
    return str(a)+","+str(b)+","+str(c)
print(name_function("Ted",50,80))

def rgb_to_hex(a,b,c):
    x=hex(a).replace('0x','')
    y=hex(b).replace('x','')
    z=hex(c).replace('x','')
    return x+y+z
print(rgb_to_hex(255,0,0))


def hex_to_rgb(a,b,c):
    x=str(int(a,16))
    y=str(int(b,16))
    z=str(int(c,16))
    return str(x)+','+str(y)+','+str(z)
print(hex_to_rgb('FF','00','00'))