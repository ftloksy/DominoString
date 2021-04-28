'''Game main module.

Contains the entry point used by the run_game.py script.

Feel free to put all your game code here, or in other modules in this "gamelib"
package.
'''

import data, game_global

def main():
#    game running
    gg = game_global.game_global()
    gg.gp.first_page(100,50)
    gg.gp.block_show_page(20)
    gg.gp.four_block_for_you_page()
    if gg.level == 5:
        gg.gp.complete_page(50,100, gg.gsf.greet_sf)
    else:
        gg.gp.complete_page(50,100, gg.gsf.the_end_title_sf)
