from os import mkdir
from shutil import rmtree

def hyphen_case(text):
    ILLEGAL_CHARS = {' ': '-', '/': '-', '&': 'and', '_': ''}
    text = text.lower()
    for char in ILLEGAL_CHARS:
        text = text.replace(char, ILLEGAL_CHARS[char])
    return text

def snake_case(text):
    return hyphen_case(text).replace('-', '_')

def read(file):
    with open(file, 'r') as file:
        content = file.read()
    return content

def write(file, *args, **kwargs):
    with open(file, 'w') as file:
        file.write(*args, **kwargs)

def pad(num, length):
    text_num = str(num)
    return ''.join(('0' * (length - len(text_num)), text_num))

def render_list(singular, plural, elements):
    base = '{}: {}'
    if len(elements) == 1:
        return base.format(singular, elements[0])
    else:
        return base.format(plural, ', '.join(elements))

def join_markdown(content):
    return ''.join(content)
