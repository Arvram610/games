class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        self.equippable = False

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
        self.equippable = True

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)


class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A regular broadsword.",
                         value=10,
                         damage=10
                         )


class Rock(Weapon):
    def __init__(self):
        super().__init__(name="Rock",
                         description="A weak as rock that can't do shit.",
                         value=0,
                         damage=2
                         )


class RustyDagger(Weapon):
    def __init__(self):
        super().__init__(name="Rusty Dagger",
                         description="It's rusty and old. Better than the rock but still weak.",
                         value=3,
                         damage=5
                         )


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="It's a dagger. It's a little worn out but it should work just fine.",
                         value=5,
                         damage=7
                         )


class Gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description=f"A coin with {str(self.amt)} stamped on front.",
                         value=self.amt)





