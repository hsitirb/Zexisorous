from modules import game
import pytest

translate_mousepos_to_filerow = game.translate_mousepos_to_filerow


testdata = [
    ((100, 100), ("a", "8")),
    ((200, 100), ("b", "8")),
    ((200, 750), ("b", "1")),
    ((750, 100), ("h", "8")),
]


@pytest.mark.parametrize("mouse_pos, expected", testdata)
def test_translate_mousepos_to_filerow(mouse_pos, expected):
    assert translate_mousepos_to_filerow(mouse_pos) == expected
