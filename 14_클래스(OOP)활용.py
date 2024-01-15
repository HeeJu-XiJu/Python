# 짱구, 짱아 게임 (like 포켓몬)
# 체력 : 나이 * 10
# 기본 데미지 남 : 7 여 : 5
# 추가 데미지 남 : 랜덤하게 액션가면공격 (+2) 여 : 랜덤하게 토끼 공격 (+5)
# 랜덤하게 짱구, 짱아 중 소리를 지르면 짱구엄마가 나타나 둘다 죽음(비김)

class Character():
    def __init__(self, name, age, gen):
        self.name = name
        self.age = age
        self.gen = gen # 남 : 액션가면 공격, 여 : 토끼인형 공격
        self.hp = age * 10

        if self.gen == 'boy':
            self.damage = 7 ####
        else :
            self.damage = 5 ####
    def attack(self, opponent):
        opponent.hp -= damage

    def check_hp(self):
        if self.hp <= 0:
            return True
        else:
            return False

class Boy (Character):
    def boy_attack1 (self, opponent):
        print(f'{self.name}가 {opponent.name}에게 {self.damage}의 피해를 주었다.')
        opponent.hp -= self.damage

    def boy_attack2 (self, opponent):
        damage = self.damage + random.randrange(0, 3, 2)
        print(f'{self.name}가 {opponent.name}에게 액션빔을 맞춰 {damage}의 피해를 주었다.')
        opponent.hp -= damage

class Girl (Character):
    def girl_attack1 (self, opponent):
        print(f'{self.name}가 {opponent.name}에게 {self.damage}의 피해를 주었다.')
        opponent.hp -= self.damage

    def girl_attack2 (self, opponent):
        damage = self.damage + random.randrange(0, 8, 7)
        print(f'{self.name}가 {opponent.name}에게 흰둥이와 함께 {damage}의 피해를 주었다.')
        opponent.hp -= damage


JJANGU = Boy('짱구', 5, 'boy')
JJANGA = Girl('짱아', 3, 'girl')

import random

while not JJANGU.check_hp() or not JJANGA.check_hp():
    random_attack = random.randint(0, 1)
    if random_attack:
        JJANGU.boy_attack2(JJANGA)
    else:
        JJANGU.boy_attack1(JJANGA)
    if JJANGA.check_hp():
        print(f'{JJANGU.name} 승리')
        break

    random_attack = random.randint(0, 1)
    if random_attack:
        JJANGA.girl_attack2(JJANGU)
    else:
        JJANGA.girl_attack1(JJANGU)
    if JJANGA.check_hp():
        print(f'{JJANGA.name} 승리')
        break

    print(f'{JJANGU.name}: {JJANGU.hp}')
    print(f'{JJANGA.name}: {JJANGA.hp}')



