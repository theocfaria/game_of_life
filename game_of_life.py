from utils import *
import os
import time

size = 20
board = randomState(int(size), int(size))
while True:
    render(board)
    board = nextTableState(board)
    time.sleep(0.5)
    os.system('cls')

    