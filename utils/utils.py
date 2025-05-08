def rgb(color: tuple[int, int, int]) -> str:
    """
    Helper utility: converts an RGB tuple to a string in the format 'rgb(r, g, b)'.

    Parameters:
    color (tuple[int, int, int]): Color in RGB format.

    Returns:
    str: CSS-formatted string 'rgb(...)'.

    Raises:
    ValueError: If any color value is not in the range 0–255.
    """
    if any(not (0 <= c <= 255) for c in color):
        raise ValueError("RGB values must be in the range 0–255.")
    return f"rgb({color[0]}, {color[1]}, {color[2]})"


def rgba(color: tuple[int, int, int, int]) -> str:
    """
    Helper utility: converts an RGBA tuple to a string in the format 'rgba(r, g, b, a)'.

    Parameters:
    color (tuple[int, int, int, int]): Color in RGBA format.

    Returns:
    str: CSS-formatted string 'rgba(...)'.

    Raises:
    ValueError: If any color value is not in the range 0–255.
    """
    if any(not (0 <= c <= 255) for c in color):
        raise ValueError("RGBA values must be in the range 0–255.")
    return f"rgba({color[0]}, {color[1]}, {color[2]}, {color[3]})"
