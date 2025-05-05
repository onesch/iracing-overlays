from utils.utils import rgb, rgba


STYLE_LABEL = "color: white; font-size: 14px; font-weight: bold;"

# colors
COLOR_THROTTLE = (44, 212, 44)
COLOR_BRAKE = (212, 44, 44)
COLOR_BACKGROUND = (0, 0, 0, 100)

# styles for telemetry
# style for bars widgets
STYLE_THROTTLE_BAR = f"""
    QProgressBar {{
        background-color: {rgba(COLOR_BACKGROUND)};
        border: none;
    }}
    QProgressBar::chunk {{
        background-color: {rgb(COLOR_THROTTLE)};
    }}
"""
STYLE_BRAKE_BAR = f"""
    QProgressBar {{
        background-color: {rgba(COLOR_BACKGROUND)};
        border: none;
    }}
    QProgressBar::chunk {{
        background-color: {rgb(COLOR_BRAKE)};
    }}
"""
# style for GRAPH
GRAPH_WIDTH = 300          # Ширина графика в пикселях
GRAPH_HEIGHT = 80          # Высота графика в пикселях
GRAPH_LEFT = 80            # Отступ слева (x-координата начала графика)
GRAPH_TOP = 40             # Отступ сверху (y-координата начала графика)
GRAPH_LINE_WIDTH = 3       # Толщина линий на графике
