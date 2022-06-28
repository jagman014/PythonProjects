import json
from typing import NamedTuple

class Player(NamedTuple):
    label: str
    colour: str


class Move(NamedTuple):
    row: int
    col: int
    label: str = ''


with open('./settings.json', 'r') as file:
    settings = json.load(file)

    BOARD_SIZE = settings['board_size']

    PLAYERS = ()
    for player, colour in settings['players'].items():
        PLAYERS += (Player(label=player, colour=colour),)
