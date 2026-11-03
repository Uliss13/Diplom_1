import pytest
from unittest.mock import Mock


class TestBurger:

    def test_init_default_values(self, burger):
        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, burger, mock_ingredient):
        mock_ing_2 = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ing_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ing_2, mock_ingredient]