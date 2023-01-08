class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def print_name(self):
        return self.name

    def hp(self):
        self.health_points *= 2
        return f'Удвоенное здоровье:{self.health_points}'

    def __str__(self):
        return f"{self.superpower}, and the superpower of {self.superpower} and {self.health_points} "

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('bob', 'lol', 'mut', 100, 'gol')
print(hero.name)
print(hero.hp())
print(hero.superpower)
print(hero.nickname)
print(len(hero.catchphrase))


class Hero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp(self):
        self.fly = True
        print(f"Здоровье нашего героя: {self.health_points ** 2}")

    def fly_sky(self):
        print(f'fly in the {self.fly}_phrase')


class SecondHero(SuperHero):
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp(self):
        self.fly = True
        print(f'Здоровье нашего героя: {self.health_points ** 2}')

    def fly_sky(self):
        print(f'fly in the {self.fly}_phrase')


thor = Hero('thor', 'bog', 'grom', 200, 'хз')
cap = SecondHero('cap', 'pon', 'hello', 150, 'ladno')
thor.hp()
thor.fly_sky()
cap.hp()
cap.fly_sky()
