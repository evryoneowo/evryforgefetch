import re

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

def visible_length(s):
    return len(ansi_escape.sub('', s))

def minimalbox(data, indent, accent, secondary, reset, title='', x=0, y=0):
    max_key_len = max(len(k) for k in data)
    max_val_len = max(len(v) for v in data.values())
    if not x:
        width = max_key_len + max_val_len + 5 - len(title)
        xindent = ''
    else:
        width = max_key_len + max_val_len + 5 - len(title)
        xindent = ' ' * (width - max_key_len - max_val_len - 5 + len(title))

    if not y:
        height = len(data)
    else:
        height = y
    
    e = width % 2

    if title:
        top = '┌' + '─' * (width // 2) + f' {title} ' + '─' * (width // 2 + e) + '┐'
        bottom = '└' + '─' * (width + len(title) + 2) + '┘'
    else:
        top = '┌' + '─' * width + '┐'
        bottom = '└' + '─' * width + '┘'

    titleindent = '  ' if title else ''

    n = 0
    lines = [top]
    for k, v in data.items():
        n += 1
        line = f'│ {accent}\x1b[1m{k.ljust(max_key_len)}\x1b[0m{reset} : {secondary}{v.ljust(max_val_len)}{reset} {titleindent}{xindent}│'
        lines.append(line)
    
    if height - n:
        for _ in range(height-n):
            lines.append(f'│{(visible_length(lines[0])-4)*" "}│')
    
    lines.append(bottom)

    return '\n'.join(lines)