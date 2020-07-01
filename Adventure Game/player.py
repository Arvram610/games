import items, world
from time import sleep as sleep
from random import randint as randint


class Player:
    def __init__(self):
        self.inventory = [items.Sword(), items.Gold(15)]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        self.equipped_weapon = [items.Rock()]

    def pickup(self):
        if not len(world.tile_exists(self.location_x, self.location_y).roomitems):
            print("There are no items to pickup.")

        else:
            print("What item do you want to pick up?\n")
            for item in world.tile_exists(self.location_x, self.location_y).roomitems:
                print(item.name)
            item = input("\nItem: ")
            for i in world.tile_exists(self.location_x, self.location_y).roomitems:
                if i.name == item:
                    self.inventory.append(i)
                    world.tile_exists(self.location_x, self.location_y).roomitems.remove(i)

                    print("You picked up {}".format(item))

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
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def equip_weapon(self):
        print("What Weapon do you want to use?")
        for i in self.inventory:
            if i.equippable:
                print(i.name)
        weapon = input(": ")
        equipped = False
        for i in self.inventory:
            if weapon == i.name and i.equippable:
                self.equipped_weapon.append(i)
                self.inventory.append(self.equipped_weapon[0])
                self.equipped_weapon.pop(0)
                self.inventory.remove(i)
                equipped = True
        if not equipped:
            print("Could not equip object: ", weapon, "\n")
        if equipped:
            print("Equipped item: ", weapon, "\n")

    def attack(self, enemy):
        max_dmg = self.equipped_weapon[0].damage
        print("You use {} against {}!".format(self.equipped_weapon[0].name, enemy.name))
        enemy.hp -= max_dmg
        sleep(1)
        if not enemy.is_alive():
            print("You defeated {}!".format(enemy.name))
        else:
            print("{} Hp is now {}. You dealt {} damage".format(enemy.name, enemy.hp, max_dmg))
        sleep(1)

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def flee(self, tile):
        available_moves = tile.adjacent_moves_flee()

        r = randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
