import logging

import config
from bot import Bot
from tower import Tower
class DarkCastleBot(Bot):

    def __init__(self):
        super().__init__()
        #self._name = 'Dark Castle Easy'

    def navigate_to(self):
        #logging.info('Navigating to map {}'.format(self._name))
        Bot.click_on(config.BUTTON_MENU_PLAY)
        Bot.click_on(config.BUTTON_MENU_MAPS_EXPERT)

        try:
            Bot.click_on(config.MAPS_DARK_CASTLE)
        except:
            Bot.click_on(config.BUTTON_MENU_MAPS_EXPERT)
            Bot.click_on(config.MAPS_DARK_CASTLE)

        Bot.click_on(config.BUTTON_MENU_DIFF_EASY)
        Bot.click_on(config.BUTTON_MENU_STANDARD_MODE)

    # Single game
    def _play_game(self):
        self._load_game(self.navigate_to)
        self._wait_for_map_load()

        Tower(self, 'hero', config.HOTKEY_HERO, config.MAPS_POS_DARK_CASTLE_INTERSECTION_TOP)

        logging.info('Starting game')
        self._start_game()

        logging.info("Waiting until round 4")
        self.wait_for(config.MAPS_ROUND_DARK_CASTLE_4)

        ninja = Tower(self, 'ninja', config.HOTKEY_TOWER_NINJA, config.MAPS_POS_DARK_CASTLE_INTERSECTION_BOTTOM)
        ninja.upgrade(1, 1)
        ninja.upgrade(3, 1)
        ninja.upgrade(1, 3)

        logging.info("Waiting until round 20")
        self.wait_for(config.MAPS_ROUND_DARK_CASTLE_20)

        super_monkey = Tower(self, 'super', config.HOTKEY_TOWER_SUPER_MONKEY, config.MAPS_POS_DARK_CASTLE_TOP_LEFT_MAIN_ROAD)
        super_monkey.upgrade(1, 2)
        super_monkey.upgrade(3, 2)

        self._wait_for_game_completion()
        self._game_completed()


if __name__ == '__main__':
    bot = DarkCastleBot()
    bot.main(required_hero='obyn')
