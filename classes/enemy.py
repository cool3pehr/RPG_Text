class Enemy:
    def __init__(self, hp, mp):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp

    def get_hp(self):
        return self.hp