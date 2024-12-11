import random
import os

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

def nextTableState(table): # it seems to be working properly when looped
    """
    rules for updating the table:
    - cell becomes 0 if has 0 or 1 neighbours and is 1.
    - cell stays 1 if has 2 or 3 neighbours and is 1.
    - cell becomes 0 if has more than 3 neighbours and is 1.
    - cell becomes 1 if is 0 and has exactly 3 neighbours.
    """
    lines = len(table)
    columns = len(table[0])
    new_table = [row[:] for row in table]  # just a copy
    
    neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(lines):
        for j in range(columns):
            neighbours_count = 0
            for dx, dy in neighbours:
                x, y = i + dx, j + dy
                if 0 <= x < lines and 0 <= y < columns:
                    neighbours_count += table[x][y]

            if table[i][j] == 1:
                if neighbours_count < 2 or neighbours_count > 3:
                    new_table[i][j] = 0 
            elif table[i][j] == 0 and neighbours_count == 3:
                new_table[i][j] = 1

    return new_table
