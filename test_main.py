import pytest
import main

def test_cell_creation():
    cell = main.Cell(0, 0)
    assert cell.row == 0
    assert cell.col == 0
    assert cell.x == 0
    assert cell.y == 0
    assert not cell.mine
    assert not cell.flagged
    assert not cell.revealed
    assert cell.adjacent_mines == 0

def test_cell_draw_revealed():
    cell = main.Cell(0, 0)
    cell.revealed = True

def test_cell_draw_flagged():
    cell = main.Cell(0, 0)
    cell.flagged = True


if __name__ == '__main__':
    # Запуск
    test_cell_creation()
    test_cell_draw_revealed()
    test_cell_draw_flagged()
