import pytest
from utils.utils import rgb, rgba


def test_rgb_valid_color():
    assert rgb((255, 0, 0)) == "rgb(255, 0, 0)"
    assert rgb((0, 255, 0)) == "rgb(0, 255, 0)"
    assert rgb((0, 0, 255)) == "rgb(0, 0, 255)"
    assert rgb((123, 45, 67)) == "rgb(123, 45, 67)"


def test_rgba_valid_color():
    assert rgba((255, 0, 0, 255)) == "rgba(255, 0, 0, 255)"
    assert rgba((0, 255, 0, 128)) == "rgba(0, 255, 0, 128)"
    assert rgba((0, 0, 255, 0)) == "rgba(0, 0, 255, 0)"
    assert rgba((10, 20, 30, 40)) == "rgba(10, 20, 30, 40)"


@pytest.mark.parametrize("color", [
    (-1, 0, 0), (0, -1, 0), (0, 0, -1),
    (256, 0, 0), (0, 256, 0), (0, 0, 256),
])
def test_rgb_invalid_color_raises(color):
    with pytest.raises(ValueError):
        rgb(color)


@pytest.mark.parametrize("color", [
    (-1, 0, 0, 255), (0, -1, 0, 255), (0, 0, -1, 255), (0, 0, 0, -1),
    (256, 0, 0, 255), (0, 256, 0, 255), (0, 0, 256, 255), (0, 0, 0, 256),
])
def test_rgba_invalid_color_raises(color):
    with pytest.raises(ValueError):
        rgba(color)
