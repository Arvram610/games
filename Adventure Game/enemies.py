class Enemy():
    def __init__(self, name, hp, damage, description):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.description = description

    def is_alive(self):
        return self.hp > 0


class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=20, damage=10, description="A handsome ogre named Shrek.")


class AngryCat(Enemy):
    def __init__(self):
        super().__init__(name="Angry Cat", hp=5, damage=2, description="It's an angry cat. Don't try to pet it")
