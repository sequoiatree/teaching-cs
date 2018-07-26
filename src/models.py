from datetime import timedelta
from os import listdir, makedirs
from os.path import join

from semester import CURRICULUM, META
from utils import *

MD_FILE_DIR = 'static/md'
TOPICAL_DIR = 'curriculum/topical'
WEEKLY_DIR = 'curriculum/weekly'
PREV_DIR, NEXT_DIR = 'prev', 'next'

RESOURCE_TYPES = {
    'readings': lambda week: None,
    'homework': lambda week: f'Due {(week.date + META["TIME_PER_HOMEWORK"]).strftime("%b %d")}',
    'journal': lambda week: None,
}

class Week():

    def __init__(self, index, topics):
        self.index = index
        self.number = self.index + 1
        self.directory = f'week-{pad(self.number, 2)}'
        self.path = f'composite-resources/{self.directory}'
        self.date = (META['SUNDAY_OF_FIRST_WEEK'] + timedelta(7) * self.index)
        self.topics = [Topic(topic) for topic in topics]
        self.title = render_list([topic.title for topic in self.topics])
        self.files = {type: [] for type in RESOURCE_TYPES}

    def load_files(self, type):
        filename = f'{type}.md'
        load_file = lambda week, path: week.files[type].append(join(path, filename))
        for topic in self.topics:
            topic_files = listdir(topic.path)
            prev_files, next_files = join(topic.path, PREV_DIR), join(topic.path, NEXT_DIR)
            if type in topic.resources:
                load_file(self, topic.path)
            if PREV_DIR in topic_files and filename in listdir(prev_files):
                load_file(WEEKS[self.index - 1], prev_files)
            if NEXT_DIR in topic_files and filename in listdir(next_files):
                load_file(WEEKS[self.index + 1], next_files)

    def load_resources(self):
        self.resources = {type: self.load_resource(type) for type in RESOURCE_TYPES}

    def load_resource(self, type):
        in_files = self.files[type]
        if in_files:
            out_dir = self.path
            out_file = self.template(type)
            makedirs(out_dir, exist_ok=True)
            if out_file not in listdir(out_dir):
                in_content = '\n\n'.join(read(in_file) for in_file in in_files)
                make_html(f'{type}', in_content, join(out_dir, out_file))
            return self.renderer(type)
        else:
            return None

    def route(self, type):
        return f'{type}-{self.number}'

    def renderer(self, type):
        return snake_case(self.route(type))

    def template(self, type):
        return f'{self.route(type)}.html'

class Topic():

    def __init__(self, topic):
        self.path = join(TOPICAL_DIR, topic)
        self.title = read(join(self.path, 'meta.txt'))
        self.chapterr = self.load_from_file('chapter.txt')
        self.resources = self.load_resources()

    def load_from_file(self, file):
        if file in listdir(self.path):
            return read(join(self.path, file))
        else:
            return None

    def load_resources(self):
        dir_files = listdir(self.path)
        return {type for type in RESOURCE_TYPES if f'{type}.md' in dir_files}

FILES = {'policies'}

WEEKS = [Week(index, topics) for index, topics in enumerate(CURRICULUM)]

for file in FILES:
    make_html('file', read(join(MD_FILE_DIR, f'{file}.md')), f'templates/{file}.html')

for week in WEEKS:
    for type in RESOURCE_TYPES:
        week.load_files(type)

for week in WEEKS:
    week.load_resources()
