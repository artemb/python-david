from games._lib.gamelib import *
from games.level09._data import conf

create_game(conf)

right()
way1 = ask()
if way1 == 'top':
    up(2)
    right()
    open_lock(44)
    right(2)
    way2 = ask()
    right(2)
    if way2 == 'top':
        up()
        open_lock(88)
        right(3)
        down(3)
    else:
        down()
        open_lock(88)
        right(3)
        down()
else:
    down(2)
    right()
    open_lock(44)
    right(2)
    way2 = ask()
    right(3)
    if way2 == 'top':
        up()
        open_lock(88)
        right(2)
        up()
    else:
        down(2)
        open_lock(88)
        right(2)
        up(4)


run()