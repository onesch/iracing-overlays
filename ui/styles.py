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
# Style for GRAPH
GRAPH_WIDTH = 300          # Width of the graph in pixels
GRAPH_HEIGHT = 80          # Height of the graph in pixels
GRAPH_LEFT = 80            # Left margin (x-coordinate of the graph start)
GRAPH_TOP = 40             # Top margin (y-coordinate of the graph start)
GRAPH_LINE_WIDTH = 3       # Line thickness in the graph
