from life_python import (
    get_neighbors,
    count_alive_neighbors,
    survives_rule,
    next_gen,
    simulation,
)

def test_get_neighborhood():
    neighbors = get_neighbors((1,1))
    assert len(neighbors) == 8
    assert (1,1) not in neighbors
    assert set(neighbors) == {(row,col) for row in (0,1,2) for col in (0,1,2)}-{(1,1)}

def test_count_alive_neighbors():
    board = [(0,0), (0,1)]
    assert count_alive_neighbors((1,1), board) == 2
    assert count_alive_neighbors((0,0), board) == 1

def test_survives_rule():
    board1 = [(0,0)]
    assert survives_rule(count_alive_neighbors((0,0), board1), (0,0), board1) == False
    board2 = [(0,0), (0,1), (1,0)]
    assert survives_rule(count_alive_neighbors((1,1), board2), (1,1), board2) == True
    assert survives_rule(count_alive_neighbors((0,0), board2), (0,0), board2) == True

def test_next_gen():
    board = [(0,1), (1,2), (2,0), (2,1), (2,2)]
    expected_board = [(1,0), (1,2), (2,1), (2,2), (3,1)]
    assert set(next_gen(board)) == set(expected_board)

def test_more_generations():
    board = [(0,1), (1,2), (2,0), (2,1), (2,2)]
    expected_board = [(25001,25002), (25000,25001), (25002,25000), (25002,25001), (25002,25002)]
    assert set(simulation(100000, board)) == set(expected_board)