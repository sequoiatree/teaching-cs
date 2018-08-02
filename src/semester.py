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
    'SLACK': 'https://cs370fall2018.slack.com/',
    'SLACK_INVITE': 'https://goo.gl/r8aG6g',
    'TUTORING_HOURS_PER_WEEK': 3,
    'TIME_UNTIL_HOMEWORK_RELEASED': timedelta(0),
    'TIME_UNTIL_JOURNAL_RELEASED': timedelta(5),
    'TIME_UNTIL_HOMEWORK_DUE': timedelta(6, 23, 59),
    'TIME_UNTIL_JOURNAL_DUE': timedelta(11, 23, 59),
    'ONE_ON_ONE_REQUESTS': 'https://goo.gl/forms/0dNV32Dnd1zHHNl62',
    'PEER_SHADOWING': 'https://goo.gl/mUeqPV',
    'TA_SHADOWING': 'https://goo.gl/NHmzMs',
    'FINAL_SURVEY': 'https://goo.gl/forms/TOyNWeMCWsrtghdw2',
}

CURRICULUM = [
    ['introduction', 'socratic-method'],
    ['learning-models', 'blooms-taxonomy'],
    ['misconception-theory', 'expert-blindness', '2-sigma'],
    ['memory', 'growth-mindset'],
    ['teaching-recursion'],
    ['setting-goals'],
    ['guest-speaker', 'flipped-classroom'],
    ['midterm', 'applying-to-staff'],
    ['group-teaching-exercise'],
    ['group-teaching-techniques', 'gps-syndrome'],
    ['imposter-syndrome', 'stereotype-threat'],
    ['diversity', 'unconscious-bias'],
    ['designing-resources'],
    ['final', 'conclusion'],
]

META['TUTORING_WEEKS'] = len(CURRICULUM)

if META['SUNDAY_OF_BREAK_WEEK']:
    CURRICULUM.insert(
        (META['SUNDAY_OF_BREAK_WEEK'] - META['SUNDAY_OF_FIRST_WEEK']).days // 7,
        ['break']
    )
    META['BREAK'] = 'Thanksgiving' if META['TERM'] == 'Fall' else 'Spring'
