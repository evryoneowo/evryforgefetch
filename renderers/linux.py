def linux(data, indent, accent, secondary, reset):
    if not data: return

    txt = ''
    for name in data:
        txt += f'{accent}{name}\n{reset}'
        for i in data[name].split('\n'):
            txt += f'>{" " * indent}{i}\n'
        txt += '\n'
    
    return txt