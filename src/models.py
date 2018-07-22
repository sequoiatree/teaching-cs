from datetime import timedelta
from os import listdir, makedirs
from os.path import join

from semester import CURRICULUM, META
from utils import *

CURRICULUM_DIR = 'curriculum'

class Week():

    def __init__(self, number, topics):
        self.number = number
        self.date = (META['SUNDAY_OF_FIRST_WEEK'] + timedelta(7) * self.number)
        self.path = f'weeks/week-{pad(self.number, 2)}'
        self.topics = [Topic(topic) for topic in topics]
        self.title = render_list([topic.title for topic in self.topics])
        self.resources = {type: self.load_resource(type) for type in RESOURCE_TYPES}

    def load_resource(self, type):
        in_files = [join(topic.path, f'{type}.md')
                    for topic in self.topics if type in topic.resources]
        if in_files:
            out_dir = self.path
            out_file = self.template(type)
            makedirs(out_dir, exist_ok=True)
            if out_file not in listdir(out_dir):
                template = read(f'templates/{type}.html')
                in_content = '\n\n'.join(read(in_file) for in_file in in_files)
                out_content = template.replace(
                    '{{ CONTENT }}',
                    in_content
                )
                write(join(out_dir, out_file), out_content)
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
        self.path = join(CURRICULUM_DIR, topic)
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

RESOURCE_TYPES = {
    'readings': lambda week: None,
    'homework': lambda week: f'Due {(week.date + META["TIME_PER_HOMEWORK"]).strftime("%b %d")}',
    'journal': lambda week: None,
}

WEEKS = [Week(number, topics) for number, topics in enumerate(CURRICULUM)]
