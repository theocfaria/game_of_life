import random

def deadState(height, width):
    dead_table = list()
    for i in range(0, height):
        dead_table.append([])
        for j in range(0, width):
            dead_table[i].append(0)
    return dead_table

def randomState(height, width):
    table_state = deadState(height, width)
    for i, lines in enumerate(table_state):
        for j, items in enumerate(lines):
            if random.random() >= 0.6:
                table_state[i][j] = 1
    return table_state

def render(table):
    for lines in table:
        print(lines)

def nextTableState(table):
    ...