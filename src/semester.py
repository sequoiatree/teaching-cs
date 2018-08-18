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
    'TIME_UNTIL_HOMEWORK_RELEASED': timedelta(0),
    'TIME_UNTIL_JOURNAL_RELEASED': timedelta(5),
    'TIME_UNTIL_HOMEWORK_DUE': timedelta(6, 23, 59),
    'TIME_UNTIL_JOURNAL_DUE': timedelta(11, 23, 59),
    'ONE_ON_ONE_REQUESTS': 'https://goo.gl/forms/0dNV32Dnd1zHHNl62',
    'PEER_SHADOWING_1': 'https://goo.gl/mUeqPV',
    'PEER_SHADOWING_2': 'https://goo.gl/3AjieE',
    'TA_SHADOWING': 'https://goo.gl/NHmzMs',
    'FINAL_SURVEY': 'https://goo.gl/forms/TOyNWeMCWsrtghdw2',
    'TUTORING_FEEDBACK': 'https://goo.gl/forms/3wPJsyHZz9Butyw52',
}

CURRICULUM_WITH_QUIZZES = [
    [['introduction', 'socratic-method'],
     'https://goo.gl/forms/rcMStCnvcQGdurtF3'],
    [['concept-mapping', 'learning-models', 'blooms-taxonomy'],
     None],
    [['misconception-theory', 'expert-blindness', '2-sigma'],
     None],
    [['memory', 'growth-mindset'],
     None],
    [['teaching-recursion'],
     None],
    [['motivation', 'setting-goals'],
     None],
    [['guest-speaker', 'flipped-classroom'],
     None],
    [['midterm', 'applying-to-staff'],
     None],
    [['group-teaching-exercise'],
     None],
    [['group-teaching-techniques', 'gps-syndrome'],
     None],
    [['imposter-syndrome', 'stereotype-threat'],
     None],
    [['diversity', 'unconscious-bias'],
     None],
    [['designing-resources'],
     None],
    [['final', 'conclusion'],
     None],
]

META['TUTORING_WEEKS'] = len(CURRICULUM_WITH_QUIZZES)

if META['SUNDAY_OF_BREAK_WEEK']:
    CURRICULUM_WITH_QUIZZES.insert(
        (META['SUNDAY_OF_BREAK_WEEK'] - META['SUNDAY_OF_FIRST_WEEK']).days // 7,
        [['break'], None]
    )
    META['BREAK'] = 'Thanksgiving' if META['TERM'] == 'Fall' else 'Spring'
