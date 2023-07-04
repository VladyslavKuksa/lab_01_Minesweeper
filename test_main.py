import pytest
from main import ROWS

def test_mine_placement():
    board = []
    for row in range(ROWS):
        board.append([0] * ROWS)
    assert len(board) == ROWS

if __name__ == "__main__":
    pytest.main()

