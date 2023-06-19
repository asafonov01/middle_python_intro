import pytest
from main import greeting


@pytest.mark.parametrize(
    'name,expected',
    [('Никита', 'Привет, Никита'), ('Ольга', 'Привет, Ольга')],
    )
def test_greeting(name: str, expected: str):
    assert greeting(name) == expected


def test_capitalize():
    name = 'яндекс практикум'
    assert greeting(name) == 'Привет, Яндекс Практикум'
