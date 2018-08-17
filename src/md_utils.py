from os import listdir
from os.path import join
from re import match

from flask import Markup
from markdown import markdown

from py_utils import *

MARKDOWN_EXTENSIONS = (
    'extra',
    'toc',
)

def make_html(template, out_file, *in_content):
    write(out_file, template_html(template, *in_content))

def template_html(template, *in_content):
    if any(in_content):
        out_content = read(f'templates/{template}.html')
        for i in range(len(in_content)):
            out_content = out_content.replace(f'{{{{ CONTENT-{i} }}}}', parse_md(in_content[i]))
        return out_content
    else:
        return ''

def read_md(file):
    return parse_md(read(file))

def parse_md(text):
    text = fix_indentation(text)
    text = md_to_html(text)
    return text

def fix_indentation(text):
    # TODO: Fix.
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        indentation = match(' +', line)
        num_spaces = len(indentation.group(0)) if indentation else 0
        lines[i] = [num_spaces, line[num_spaces:]]
    for i in range(len(lines)):
        num_spaces, line = lines[i]
        if num_spaces > 0:
            if match('\d\. ', lines[i - 1][1]):
                indentation_factor = 3
            elif match('\* ', lines[i - 1][1]):
                indentation_factor = 2
            else:
                indentation_factor = None
            if indentation_factor:
                lines[i][0] = 4 * num_spaces // indentation_factor
    return '\n'.join([' ' * num_spaces + line for num_spaces, line in lines])

def md_to_html(text):
    return markdown(text, extensions=MARKDOWN_EXTENSIONS, output_format='html5')

def read_bio(name, directory):
    jpg, png, imgs = f'{name}.jpg', f'{name}.png', listdir('static/img')
    img = jpg if jpg in imgs else png if png in imgs else 'staff.jpg'
    with open(f'staff/{directory}/{name}.md', 'r') as file:
        name = file.readline().strip('\n')
        file.readline()
        email = file.readline().strip('\n')
        file.readline()
        bio = parse_md(file.readline()).strip('\n')
        file.readline()
        website = file.readline().strip('\n')
    info = {
        'img': img,
        'name': name,
        'email': make_link(email, f'mailto:{email}'),
        'bio': bio,
        'website': website,
        'link': make_link(name, website),
    }
    return {key: Markup(val) for key, val in info.items()}

def make_link(text, link):
    return f'<a href="{link}">{text}</a>' if link else text
