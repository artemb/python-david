from games._lib.gamelib import *
from games.level06._data import conf

create_game(conf)

right()
ask()
right(3)
lock = look()
if lock == 'orange lock':
    open_lock(7)
else:
    open_lock(15)
right(5)

run()