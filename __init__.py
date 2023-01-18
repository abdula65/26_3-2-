from classs import Hero, Hero_super

hero1 = Hero_super('bum', 'von')
hero2 = Hero('durr', 'mutation')
print(hero1.get_name())
print(hero1.power())


from turtle import *
color("green")
bgcolor("black")
speed(11)
hideturtle()
b = 0
while b < 200:
    right(b)
    forward(b * 3)
    b = b + 1