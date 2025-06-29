import re

def strip_ansi(text):
    return re.sub(r'\x1b\[([0-9]+)(;[0-9]+)*m', '', text)

def gradient(text, start_color='\033[38;5;33m', end_color='\033[38;5;39m'):
    start = 33
    end = 39
    length = len(text)
    if length == 0:
        return ''

    result = ''
    for i, c in enumerate(text):
        color_code = int(start + (end - start) * i / (length - 1))
        result += f'\033[38;5;{color_code}m{c}'
    result += '\033[0m'
    return result

def colorwave(data, indent, accent, secondary, reset):
    lines = []
    indent_space = ' ' * indent

    for key, value in data.items():
        key_colored = gradient(key, start_color=accent, end_color=secondary)
        val_str = str(value)

        val_colored = f"{accent}{val_str}{reset}"

        lines.append(f"{indent_space}{key_colored}: {val_colored}")
        underline_len = len(strip_ansi(key)) + 2 + len(strip_ansi(val_str))
        underline = ''.join(
            f'\033[38;5;{33 + (i % 7)}m─{reset}' for i in range(underline_len)
        )
        lines.append(f"{indent_space}{underline}")

    return '\n'.join(lines)
