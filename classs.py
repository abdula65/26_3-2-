class Hero:
    people = 'people'

    def __init__(self, name, ability):
        self.name = name
        self.ability = ability


class Hero_super(Hero):
    people = 'people'
    def __init__(self, name, ability):
        super().__init__(name, ability)
        self.name = name
        self.ability = ability

    def __str__(self):
        return {self.name}

    def get_name(self):
        return f'it is super_hero: {self.name}'

    def power(self):
        return f'Способность: {self.ability}'

Sup = Hero_super('Bum', 'speed')
print(Sup.get_name())
print(Sup.power())