import player as plr


class Action:
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=plr.Player.flee, name="Flee", hotkey="f", tile=tile)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=plr.Player.move_north, name='Move north', hotkey='n')


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=plr.Player.move_south, name='Move south', hotkey='s')


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=plr.Player.move_east, name="Move East", hotkey="e")


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=plr.Player.move_west, name="Move West", hotkey="w")


class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=plr.Player.print_inventory, name="View Inventory", hotkey="i")


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=plr.Player.attack, name="Attack", hotkey="a", enemy=enemy)


class ChangeWeapon(Action):
    def __init__(self):
        super().__init__(method=plr.Player.equip_weapon, name="Equip", hotkey="e")


class Pickup(Action):
    def __init__(self):
        super().__init__(method=plr.Player.pickup, name="Pickup", hotkey="p")
