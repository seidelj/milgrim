import os, csv
import website.wsgi
from django.conf import settings


from nodes.models import Path, Decision, Meter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csvFile = os.path.join(BASE_DIR, 'meters.csv')

with open(csvFile) as f:
    csvreader = csv.reader(f)
    csvreader.next()
    for row in csvreader:
        path, created = Path.objects.get_or_create(name=row[0])
        decision, created = Decision.objects.get_or_create(path_id=path.id,event=row[1])
        health, created = Meter.objects.get_or_create(decision_id=decision.id, name="health", value=row[2])
        money, created = Meter.objects.get_or_create(decision_id=decision.id, name="money", value=row[3])
        social, created = Meter.objects.get_or_create(decision_id=decision.id, name="social", value=row[4])
