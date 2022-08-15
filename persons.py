class Character:
    '''
    Базовый класс для создания персонажа
    '''
    def __init__(self, name='', attack=0, defence=0, magic=0):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.magic = magic

    def __repr__(self):
        return 'Character: ' + \
               'Attack: ' + \
               str(self.attack) + \
               ', ' + \
               'Defence: ' + \
               str(self.defence) + \
               ', ' + \
               'Magic: ' + \
               str(self.magic)

    def attack_creature(self, power, creature):
        '''

        :param power: Сила атаки на существо
        :param creature: Существо, на которое нападаем
        :return: True если существо убито
        '''
        return 'shit'


todd = Character('Todd', 5, 10, 20)
todd.attack_creature()

print(todd)
