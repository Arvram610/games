import items, world, enemies
from time import sleep as sleep


class Player:
    def __init__(self):
        self.inventory = [items.Sword(), items.Gold(15)]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        self.equipped_weapon = [items.Rock()]

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        if len(self.inventory) != 0:
            print("Inventory:")
            for item in self.inventory:
                print(item, "\n")
        print(f"Holding: \n{self.equipped_weapon[0]}")

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text)

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def equip_weapon(self, weapon):
        equipped = False
        for i in self.inventory:
            if weapon == i.name and i.equippable:
                self.equipped_weapon.append(i)
                self.inventory.append(self.equipped_weapon[0])
                self.equipped_weapon.pop(0)
                self.inventory.remove(i)
                equipped = True
        if not equipped:
            print("Could not equip object: ", weapon,"\n")
        if equipped:
            print("Equipped item: ", weapon, "\n")


    def attack(self, enemy):
        max_dmg = self.equipped_weapon[0].damage
        print("You use {} against {}!".format(self.equipped_weapon[0].name, enemy.name))
        enemy.hp -= max_dmg
        sleep(1)
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} Hp is {}.".format(enemy.name, enemy.hp))
        sleep(1)

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)