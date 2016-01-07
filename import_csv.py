import os, csv
import website.wsgi
from django.conf import settings


from nodes.models import Path, Decision

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csvFile = os.path.join(BASE_DIR, 'meters.csv')

with open(csvFile) as f:
    csvreader = csv.reader(f)
    csvreader.next()
    for row in csvreader:
        path, created = Path.objects.get_or_create(name=row[0])
        print path
        decision, created = Decision.objects.get_or_create(path_id=path.id,event=row[1])
        decision.health = row[2]
        decision.money = row[3]
        decision.social = row[4]
        decision.save()
