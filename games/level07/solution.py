from games._lib.gamelib import *
from games.level07._data import conf

create_game(conf)

right(1)
lock1 = ask()
if lock1 == 'bottom':
    down()
else:
    up()

right(3)
open_lock(7)
right(3)

if lock1 == 'bottom':
    up()
else:
    down()


lock2 = ask()

if lock2 == 'bottom':
    down()
else:
    up()

right(3)
open_lock(9)
right(4)
if lock2 == 'bottom':
    up()
else:
    down()

run()