import enemies, items, actions, world

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast)
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest)
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth)
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth)
        return moves

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.ChangeWeapon())

        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return"""
StartRoom
        """

    def modify_player(self, player):
        # nothing happens
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x,y)

    def modify_player(self, player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, the_player.hp))


class EmptyRoom(MapTile):
    def intro_text(self):
        return """
An empty room.
        """
    def modify_player(self, player):
        pass


class AngryCatRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.AngryCat)

    def intro_text(self):
        if self.enemy.is_alive():
            return """
Suddenly ANGRY CAT!
            """
        else:
            return """
A rotting Corpse of a once angry cat.
            """


class FindRustyDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.RustyDagger)

    def intro_text(self):
        return """
Wow there is a Rusty Dagger on the floor. \nYou pick it up.
        """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger)

    def intro_text(self):
        return """
There is a Dagger on the floor. Things are looking brighter! \nYou pick it up.
        """


class FindSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger)

    def intro_text(self):
        return """
There is a Sword on the floor. With this you will be unstoppable!!! \nYou pick it up.
        """

