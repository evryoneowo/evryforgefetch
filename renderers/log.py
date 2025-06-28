def log(data, indent, accent, secondary, reset):
    if not data: return

    txt = ''
    for name in data:
        txt += f'{accent}[{secondary}{name.upper()}{accent}]{reset}'
        txt += f'{" " * indent}{data[name].split('\n')[0]}\n'
        for i in data[name].split('\n')[1:]:
            txt += f'{" " * (len(name) + 2 + indent)}{i}\n'
        txt += '\n'
    
    return txt