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

def nextTableState(table):
    """
    Atualiza uma tabela de células com base nas regras fornecidas:
    - Célula se torna 0 se tiver 0 ou 1 vizinhos iguais a 1 e ela mesma for 1.
    - Célula permanece 1 se tiver 2 ou 3 vizinhos iguais a 1 e ela mesma for 1.
    - Célula se torna 0 se tiver mais de 3 vizinhos iguais a 1 e ela mesma for 1.
    - Célula se torna 1 se for 0 e tiver exatamente 3 vizinhos iguais a 1.
    """
    lines = len(table)
    columns = len(table[0])
    new_table = [row[:] for row in table]  # cópia de segurança
    
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