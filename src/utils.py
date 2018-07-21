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

def render_list(elements, singular=None, plural=None):
    if len(elements) == 1:
        text = elements[0]
    elif len(elements) == 2:
        text = f'{elements[0]} and {elements[1]}'
    else:
        text = '{}, and {}'.format(', '.join(elements[:-1]), elements[-1])
    if singular or plural:
        assert singular and plural, 'Please specify and singular and plural base.'
        return '{}: {}'.format(singular if len(elements) == 1 else plural, text)
    else:
        return text

def join_markdown(content):
    return ''.join(content)
