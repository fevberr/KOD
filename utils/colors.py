import os
import sys
import platform
import json
import time
import re

COLORS_FILE = "color_settings.json"

DEFAULT_COLORS = {
    "primary": "GREEN",
    "secondary": "CYAN",
    "success": "GREEN",
    "error": "RED",
    "warning": "YELLOW",
    "info": "BLUE",
    "highlight": "MAGENTA",
    "dim": "GRAY",
    "prompt": "GREEN",
    "border": "CYAN"
}

COLOR_CODES = {
    "BLACK": '\033[30m', "RED": '\033[31m', "GREEN": '\033[32m',
    "YELLOW": '\033[33m', "BLUE": '\033[34m', "MAGENTA": '\033[35m',
    "CYAN": '\033[36m', "WHITE": '\033[37m',
    "BRIGHT_RED": '\033[91m', "BRIGHT_GREEN": '\033[92m',
    "BRIGHT_YELLOW": '\033[93m', "BRIGHT_BLUE": '\033[94m',
    "BRIGHT_MAGENTA": '\033[95m', "BRIGHT_CYAN": '\033[96m',
    "BRIGHT_WHITE": '\033[97m', "GRAY": '\033[90m',
    "PURPLE": '\033[95m', "ORANGE": '\033[38;5;208m',
    "PINK": '\033[38;5;201m', "LIME": '\033[38;5;154m',
    "TEAL": '\033[38;5;37m', "GOLD": '\033[38;5;220m',
    "SILVER": '\033[38;5;250m', "BROWN": '\033[38;5;130m',
    "RESET": '\033[0m', "BOLD": '\033[1m', "DIM": '\033[2m'
}

ALL_COLORS = ["GREEN", "RED", "CYAN", "YELLOW", "BLUE", "MAGENTA", "GRAY", "WHITE", 
              "BLACK", "BRIGHT_GREEN", "BRIGHT_RED", "BRIGHT_CYAN", "BRIGHT_YELLOW",
              "BRIGHT_BLUE", "BRIGHT_MAGENTA", "BRIGHT_WHITE",
              "PURPLE", "
