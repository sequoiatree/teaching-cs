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
    'readings': lambda wk: f'Wk. {pad(wk.number, 2)}',
    'homework': lambda wk: f'Due {(wk.date + META["TIME_UNTIL_HOMEWORK_DUE"]).strftime("%b %d")}',
    'tutoring': lambda wk: f'Due {(wk.date + META["TIME_UNTIL_JOURNAL_DUE"]).strftime("%b %d")}',
}

RESOURCE_TEMPS = {
    'readings': ['readings'],
    'homework': ['homework'],
    'tutoring': ['assignment', 'journal'],
}

RESOURCE_FILES = sum(RESOURCE_TEMPS.values(), [])

class Week():

    def __init__(self, index, topics):
        self.index = index
        self.number = self.index + 1
        self.directory = f'week-{pad(self.number, 2)}'
        self.path = f'composite-resources/{self.directory}'
        self.date = (META['SUNDAY_OF_FIRST_WEEK'] + timedelta(7) * self.index)
        self.topics = [Topic(topic) for topic in topics]
        self.title = render_list([topic.title for topic in self.topics])
        self.files = {type: [] for type in RESOURCE_FILES}

    def load_files(self, type):
        filename = f'{type}.md'
        load_file = lambda week, path: week.files[type].append(join(path, filename))
        weekly_path = join(WEEKLY_DIR, self.directory)
        if self.directory in listdir(WEEKLY_DIR) and filename in listdir(weekly_path):
            load_file(self, weekly_path)
        for topic in self.topics:
            prev_path, next_path = join(topic.path, PREV_DIR), join(topic.path, NEXT_DIR)
            topic_files = listdir(topic.path)
            if type in topic.resources:
                load_file(self, topic.path)
            if PREV_DIR in topic_files and filename in listdir(prev_path):
                load_file(WEEKS[self.index - 1], prev_path)
            if NEXT_DIR in topic_files and filename in listdir(next_path):
                load_file(WEEKS[self.index + 1], next_path)

    def load_resources(self):
        self.resources = {template: self.load_resource(template, *RESOURCE_TEMPS[template])
                          for template in RESOURCE_TEMPS}

    def load_resource(self, template, *types):
        files_by_type = [self.files[type] for type in types]
        if any(files_by_type):
            out_dir = self.path
            out_file = self.template(template)
            makedirs(out_dir, exist_ok=True)
            if out_file not in listdir(out_dir):
                in_content = ['\n\n'.join(read(file) for file in files) for files in files_by_type]
                make_html(f'{template}', join(out_dir, out_file), *in_content)
            return self.renderer(template)
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
        return {type for type in RESOURCE_FILES if f'{type}.md' in dir_files}

FILES = {'policies'}

WEEKS = [Week(index, topics) for index, topics in enumerate(CURRICULUM)]

for file in FILES:
    make_html('file', f'templates/{file}.html', read(join(MD_FILE_DIR, f'{file}.md')))

for week in WEEKS:
    for type in RESOURCE_FILES:
        week.load_files(type)

for week in WEEKS:
    week.load_resources()
