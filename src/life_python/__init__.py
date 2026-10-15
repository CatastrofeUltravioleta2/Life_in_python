def add_glider(board, glider):
    board.update((row,col) for row, col in glider)

def get_neighbors(cell):
    offsets = [-1,0,1]
    return [(cell[0]+dx, cell[1]+dy) for dy in offsets for dx in offsets if (dx, dy) != (0, 0)]

def count_alive_neighbors(cell, alive_cells):
    return sum(1 for acell in get_neighbors(cell) if acell in alive_cells)

def survives_rule(count, cell, alive_cells):
    return (count == 3 or count == 2 and cell in alive_cells)

def next_gen(alive_cells):
    alive_cells = set(alive_cells)
    all_neighbors = {ncell for cell in alive_cells for ncell in get_neighbors(cell)}
    return {cell for cell in all_neighbors if survives_rule(count_alive_neighbors(cell, alive_cells), cell, alive_cells)}

def print_cells(alive_cells):
    for row, col in sorted(alive_cells):
        print(f"({row},{col})")

def simulation(iterations, board):
    board = set(board)
    for i in range(iterations): 
        board = next_gen(board)
    return board

def main():
    board = set()
    initial_glider = [(0,1), (1,2), (2,0), (2,1), (2,2)]
    add_glider(board, initial_glider)
    final_board = simulation(1, board)
    print_cells(final_board)