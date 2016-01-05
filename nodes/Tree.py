

class Node(object):

    childrenDict = {
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

    def get_description(prob):
        if prob >= 90:
            return "Highly Probably"
        elif prob >= 75:
            return "Quite Likely"
        elif prob >= 65:
            return "Rather Likely"
        elif prob >= 56:
            return "Better Than Even"
        elif prob >= 46:
            return "Toss-up"
        elif prob >= 40:
            return "Uncertain"
        elif prob > 10:
            return "Not very Probable"
        else:
            return "Very Unlikely"


    probabilityDict = {
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

    def __init__(self, tree, event):
        if event == 0:
            self.event = tree
        else:
            self.event = events[event]
        self.probability = probabilityDict[tree][event]
        self.description = get_description(self.probability)
        self.children = childrenDict[event]
