from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Path(models.Model):
    name = models.CharField(max_length=128)

    def get_meters(self, event):
        decision = self.decision_set.filter(event=event)[0]
        return decision.meter_set.all()

    def get_parent_meters(self, event):
        parent = None
        for key, value in Constants.children.items():
            if event in value:
                parent = key
        if not parent:
            parent = 0
        decision = self.decision_set.filter(event=parent)[0]
        return decision.meter_set.all()

class Decision(models.Model):
    path = models.ForeignKey(Path)
    event = models.IntegerField(null=True)


class Meter(models.Model):
    decision = models.ForeignKey(Decision)
    name = models.CharField(max_length=256)
    value = models.IntegerField(null=True)

    def get_color(self):
        if self.name == "wage":
            return "success"
        elif self.name == "welfare":
            return "warning"
        elif self.name == "prison":
            return "danger"

    def get_icon(self):
        if self.name == "wage":
            return "https://maxcdn.icons8.com/windows8/PNG/26/Finance/USD-26.png"
        if self.name == "welfare":
            return "https://maxcdn.icons8.com/iOS7/PNG/25/Finance/receive_cash-25.png"
        if self.name == 'prison':
            return "https://maxcdn.icons8.com/windows8/PNG/26/City/prisoner-26.png"
        return None

    def get_description(self):
        if self.name == "wage":
            return "This meter how much money you could make compared to a high school drop out, the MORE filled the better!"
        if self.name == "welfare":
            return "This meter shows how reliant you may become on the state for assistance, the LESS filled the better!"
        if self.name == "prison":
            return "This meter shows how likely you could be to having to spend time behind bars compared to a highschool dropout, the LESS filled the better!"

class Constants:
    trees = [
        ['highC', "A-B Student", "You receive high grades and are at the top of your class!"],
        ['medC', "Average Student", "You recieve mostly C grade"],
        ['highNc', "Hard Worker", "You always complete all of your school work, no matter what!"],
        ['medNc', "Average Worker", "You do most of your homework"],
    ]

    children = {
        0: [1,2],
        1: [3,6],
        2: [7,8],
        3: [4,5],
        4: [9],
        5: [10],
        6: [11],
        7: [12],
        8: [13],
        9: [],
        10:[],
        11:[],
        12:[],
        13:[],
    }

    probabilities = {
        'highC': [
            82, 18, 49, 38, 62, 51,
            75, 25, None, None, None,
            None, None,
        ],
        'medC': [
            68, 32, 37, 27, 73, 63,
            58, 42, None, None, None,
            None, None,
        ],
        'lowC': [
            59, 41, 20, 25, 75, 80,
            25, 75, None, None, None,
            None, None,
        ],
        'highNc': [
            85, 15, 47, 39, 61, 53,
            65, 45, None, None, None,
            None, None,
        ],
        'medNc': [
            68, 32, 37, 27, 73, 63,
            58, 42, None, None, None,
            None, None,
        ],
        'lowNc': [
            52, 48, 36, 34, 66, 64,
            60, 40, None, None, None,
            None, None,
        ],
    }




    events = [
        "Graduate High School",
        "Drop out of High School",
        "Attend College",
        "Graduate College",
        "Drop out of 4-year College",
        "Do not attend College",
        "Take GED",
        "Remain High School Dropout",
        "4-year College graduate",
        "Some College",
        "High School graduate",
        "GED",
        "Drop-out",
    ]




