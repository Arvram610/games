import player

class Action:
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=player.move_north, name="Move North", hotkey="n")


class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=player.move_south, name="Move South", hotkey="s")


class MoveEast(Action):
    def __init__(self):
        super().__init__(method=player.move_east, name="Move East", hotkey="e")


class MoveWest(Action):
    def __init__(self):
        super().__init__(method=player.move_west, name="Move West", hotkey="w")


class ViewInventory(Action):
    def __init__(self):
        super().__init__(method=player.print_inventory(),name="View Inventory", hotkey="i")


class Attack(Action):
    def __init__(self):
        super().__init__(method=player.attack, name="Attack", hotkey="a", enemy=enemy)


class ChangeWeapon(Action):
    def __init__(self):
        super().__init__(method=player.equip_weapon, name="Equip", hotkey="e", weapon=weapon)