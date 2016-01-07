from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Constants:
    trees = [
        'highC',
        'medC',
        'lowC',
        'highNc',
        'medNc',
        'lowNc',
    ]

    children = {
        0: [1,2],
        1: [3,4],
        2: [5,6],
        3: [7,8],
        4: [11],
        5: [12],
        6: [13],
        7: [9],
        8: [10],
        9: [],
        10:[],
        11:[],
        12:[],
        13:[],
    }

    probabilities = {
        'highC': [
            90, 10, 65, 35, 80, 20,
            63, 37, None, None, None,
            None, None,
        ],
        'medC': [
            80, 20, 42, 58, 53, 47,
            43, 57, None, None, None,
            None, None,
        ],
        'lowC': [
            59, 41, 20, 80, 25, 57,
            25, 75, None, None, None,
            None, None,
        ],
        'highNc': [
            90, 19, 54, 46, 60, 40,
            56, 44, None, None, None,
            None, None,
        ],
        'medNc': [
            80, 20, 47, 53, 60, 40,
            46, 54, None, None, None,
            None, None,
        ],
        'lowNc': [
            52, 48, 36, 64, 60, 40,
            34, 66, None, None, None,
            None, None,
        ],
    }

    events = [
        "Graduate High School",
        "Drop out of High School",
        "Attend College",
        "Do not attend College",
        "Take GED",
        "Remain High School Dropout",
        "Graduate College",
        "Drop out of 4-year College",
        "4-year College graduate",
        "Some College",
        "High School graduate",
        "GED",
        "Drop-out",
    ]


