def text_index_advance(index: str, offset: str):
    a, b = index.split('.')
    c, d = offset.split('.')
    return f'{int(a)+int(c)}.{int(b)+int(d)}'