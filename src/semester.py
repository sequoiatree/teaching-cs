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
    'STAFF': {
        'instructors': ['christopher-hunn', 'sequoia-eyzaguirre', 'bryan-tong'],
        'teaching-interns': sorted({
            'asli-akalin',
            'cesar-plascencia-zuniga',
            'griffin-prechter',
            'jade-singh',
            'jessica-lee',
            'rina-lu',
        })
    },
    'SCHEDULER': 'http://cs370scheduler.org',
    'SLACK': 'https://cs370fall2018.slack.com/',
    'SLACK_INVITE': 'https://goo.gl/Cq1cma',
    'TUTORING_HOURS_PER_WEEK': 3,
    'TUTORING_HOURS_PER_WEEK_TA': 1,
    'TIME_UNTIL_HOMEWORK_DUE': timedelta(6, 23, 59),
    'TIME_UNTIL_JOURNAL_DUE': timedelta(6, 23, 59),
    'ONE_ON_ONE_REQUESTS': 'https://goo.gl/forms/0dNV32Dnd1zHHNl62',
    'PEER_SHADOWING_1': 'https://goo.gl/mUeqPV',
    'PEER_SHADOWING_2': 'https://goo.gl/3AjieE',
    'TA_SHADOWING': 'https://goo.gl/NHmzMs',
    'FINAL_SURVEY': 'https://goo.gl/forms/TOyNWeMCWsrtghdw2',
    'TUTORING_FEEDBACK': 'https://goo.gl/forms/3wPJsyHZz9Butyw52',
}

TIME_UNTIL_RELEASED = {
    # Relative to the start of the week on Sunday at 12:00 AM.
    'homework': timedelta(-1),
    'tutoring': timedelta(-1),
}

CURRICULUM_WITH_SIGNUPS = [
    [['introduction', 'socratic-method'],
     None],
    [['concept-mapping', 'learning-models', 'blooms-taxonomy'],
     'https://goo.gl/dkZahs'],
    [['misconception-theory', 'expert-blindness', '2-sigma'],
     'https://goo.gl/eYx2cW'],
    [['memory', 'growth-mindset'],
     'https://goo.gl/ooPZgp'],
    [['teaching-recursion'],
     'https://goo.gl/Z3obtd'],
    [['motivation', 'setting-goals'],
     'https://goo.gl/UCG2dd'],
    [['guest-speaker', 'flipped-classroom'],
     'https://goo.gl/FXzCqf'],
    [['midterm', 'applying-to-staff'],
     'https://goo.gl/bD5gS6'],
    [['group-teaching-exercise'],
     'https://goo.gl/4A5jU8'],
    [['group-teaching-techniques', 'gps-syndrome'],
     'https://goo.gl/ng5ABy'],
    [['imposter-syndrome', 'stereotype-threat'],
     'https://goo.gl/YwutRP'],
    [['diversity', 'unconscious-bias'],
     'https://goo.gl/zA9VHh'],
    [['designing-resources'],
     'https://goo.gl/ftfYWg'],
    [['final', 'conclusion'],
     'https://goo.gl/U24B4H'],
]

META['TUTORING_WEEKS'] = len(CURRICULUM_WITH_SIGNUPS)

if META['SUNDAY_OF_BREAK_WEEK']:
    CURRICULUM_WITH_SIGNUPS.insert(
        (META['SUNDAY_OF_BREAK_WEEK'] - META['SUNDAY_OF_FIRST_WEEK']).days // 7,
        [['break'], None]
    )
    META['BREAK'] = 'Thanksgiving' if META['TERM'] == 'Fall' else 'Spring'
