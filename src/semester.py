from datetime import datetime, timedelta

from flask import Markup

from utils import *

META = {
    'CLASS_CODE': 'CS 370',
    'CLASS_NAME': 'Introduction to Teaching Computer Science',
    'YEAR': '2018',
    'TERM': 'Fall',
    'SUNDAY_OF_FIRST_WEEK': datetime(2018, 8, 19),
    'SUNDAY_OF_BREAK_WEEK': datetime(2018, 11, 18), # None if there's no break.
    'INSTRUCTOR': Markup(render_list([
        'Christopher Hunn',
        make_link('Sequoia Eyzaguirre', 'https://sequoia-tree.github.io'),
    ], 'Instructor', 'Instructors')),
    'SCHEDULER': 'http://cs370scheduler.org',
    'PIAZZA': 'https://piazza.com/class/jjvyvwze5n58k',
    'TIME_UNTIL_HOMEWORK_RELEASED': timedelta(0), # TODO
    'TIME_UNTIL_JOURNAL_RELEASED': timedelta(0), # TODO
    'TIME_PER_HOMEWORK': timedelta(6, 23, 59),
    'TIME_PER_JOURNAL': timedelta(0), # TODO
}

CURRICULUM = [
    ['introduction', 'socratic-method'],
    ['learning-models', 'blooms-taxonomy'],
    ['misconception-theory', '2-sigma'],
    ['memory', 'growth-mindset'],
    ['teaching-recursion'],
    ['setting-goals'],
    ['guest-speaker'],
    ['midterm', 'applying-to-staff'],
    ['group-teaching-exercise'],
    ['group-teaching-techniques', 'gps-syndrome'],
    ['imposter-syndrome', 'stereotype-threat'],
    ['diversity'],
    ['designing-resources'],
    ['conclusion'],
]

if META['SUNDAY_OF_BREAK_WEEK']:
    CURRICULUM.insert(
        (META['SUNDAY_OF_BREAK_WEEK'] - META['SUNDAY_OF_FIRST_WEEK']).days // 7,
        ['break']
    )
