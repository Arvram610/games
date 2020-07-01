import enemies, items, actions, world
from time import sleep as wait


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.roomitems = []
        self.discovered = False

    def roomitems_add(self, roomitems):
        for i in roomitems:
            self.roomitems.append(i)

    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, the_player):
        raise NotImplementedError()

    def adjacent_moves(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def adjacent_moves_flee(self):
        moves = []
        if world.tile_exists(self.x + 1, self.y) and world.tile_exists(self.x + 1, self.y).discovered:
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y) and world.tile_exists(self.x - 1, self.y).discovered:
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1) and world.tile_exists(self.x, self.y - 1).discovered:
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1) and world.tile_exists(self.x, self.y + 1).discovered:
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.ChangeWeapon())
        return moves


class StartingRoom(MapTile):
    def intro_text(self):
        return"""
It's a dead end.
        """

    def modify_player(self, the_player):
        # nothing happens
        self.discovered = True


class LootRoom(MapTile):
    def __init__(self, x, y, items):
        self.items = items
        self.additems = False
        super().__init__(x, y)

    def intro_text(self):
        pass

    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        moves.append(actions.ChangeWeapon())
        if not len(self.roomitems) == 0:
            moves.append(actions.Pickup())

        return moves

    def modify_player(self, the_player):
        self.discovered = True
        if not self.additems:

            self.roomitems_add(self.items)
            self.additems = True


class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def available_actions(self):
        moves = []
        if self.enemy.is_alive():
            moves.append(actions.Attack(self.enemy))
            moves.append(actions.Flee(tile=self))

        else:
            moves = self.adjacent_moves()
            moves.append(actions.ViewInventory())
            moves.append(actions.ChangeWeapon())

        return moves

    def intro_text(self):
        pass

    def modify_player(self, the_player):
        self.discovered = True
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.\n".format(self.enemy.damage, the_player.hp))
            wait(1)


class EmptyRoom(MapTile):
    def intro_text(self):
        return """
An empty room.
        """

    def modify_player(self, the_player):
        self.discovered = True
        pass


class AngryCatRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.AngryCat())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
You enter the room when: Suddenly an ANGRY CAT appears!!!
            """
        else:
            return """
The room contains a rotting Corpse of a once angry cat.
            """


class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
You enter the room when: Suddenly A handsome Ogre appears!!!
                """
        else:
            return """
The room contains a rotting corpse of an Ogre.
                """


class FindRustyDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, items=[items.RustyDagger()])

    def intro_text(self):
        return """
Wow there is a Rusty Dagger on the floor. \nYou pick it up.
        """


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, items=[items.Dagger()])

    def intro_text(self):
        if not len(self.items) == 0:
            return """
There is a Dagger on the floor. Hallelujah!
            """
        else:
            return """
It's another empty room.            
            """


class FindSwordRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x=x, y=y, items=[items.Sword()])

    def intro_text(self):
        if not len(self.items) == 0:
            return """
There is a Sword on the floor. With this you will be unstoppable!!!
            """
        else:
            return """
It's another empty room.            
                    """


class ExitRoom(MapTile):
    def intro_text(self):
        return """
        You survived the swamp. Time to write a movie about the ogre you met.
        """

    def modify_player(self, the_player):
        the_player.victory = True
