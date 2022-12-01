import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'using_models.settings')

import django

django.setup()

# FAKE Population Script
import random
from first_app.models import *
from faker import Faker

fakegen = Faker()
topics = [
    'Search',
    'Social',
    'Marketplace',
    'News',
    'Games'
]

def add_topic() -> Topic:
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    
    return t

def populate(N: int=5) -> None:
    for entry in range(N):
        # get topic for fake entry
        top = add_topic()

        # add fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create new webpage entry
        webpg = Webpage.objects.get_or_create(
            topic=top, 
            url=fake_url, 
            name=fake_name
        )[0]

        # create new access record
        acc_rec = AccessRecord.objects.get_or_create(
            name=webpg,
            date=fake_date
        )[0]

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populated')
