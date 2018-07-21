from utils import *

SEMESTER = {
    'CLASS_CODE': 'CS 370',
    'CLASS_NAME': 'Introduction to Teaching Computer Science',
    'YEAR': '2018',
    'TERM': 'Fall',
    'INSTRUCTOR': render_list('Instructor', 'Instructors', [
        'Christopher Hunn',
        'Sequoia Eyzaguirre',
    ]),
}

CURRICULUM = [
    ['introduction', 'socratic-method'],
    ['learning-models'],
    ['misconception-theory', '2-sigma'],
    ['memory', 'growth-mindset'],
    ['teaching-recursion'],
    ['setting-goals'],
    ['guest-speaker'],
    ['midterm'],
    ['group-teaching-exercise'],
    ['group-teaching-models', 'gps-syndrome'],
    ['imposter-syndrome', 'stereotype-threat'],
    ['diversity'],
    ['material-design'],
    ['conclusion'],
]

CURRICULUM = [['socratic-method']] # TESTING PURPOSES
