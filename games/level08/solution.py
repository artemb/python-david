from games._lib.gamelib import *
from games.level08._data import conf

create_game(conf)

right()
lock = ask()
if lock == 'top':
    up(3)
    right(3)
    down(2)
    right()
    open_lock(19)
    right(3)
    down()
else:
    down(3)
    right(5)
    up(2)
    open_lock(19)
    right(2)
    up()

run()