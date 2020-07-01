import world
import player as plr
from time import sleep as wait


def play():
    world.load_tiles()
    player = plr.Player()
    room = world.tile_exists(player.location_x, player.location_y)
    print("You find yourself in a dark and quiet Swamp, In the distance you can hear a faint tune of All Star playing.\n")
    wait(1)
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            done_action = False
            while not done_action:
                print("Choose an action:\n")
                wait(1)
                available_actions = room.available_actions()
                for action in available_actions:
                    print(action)
                    wait(0.5)
                action_input = input('Action: ')
                for action in available_actions:
                    if action_input == action.hotkey:
                        done_action = True
                        player.do_action(action, **action.kwargs)
                        break


if __name__ == "__main__":
    play()
