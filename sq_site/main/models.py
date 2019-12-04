from django.db import models
from datetime import datetime

class Visitors(models.Model):

    def congratuldations(self):
        if self.id % 10 == 0:
            return 'Hooray!'
        else:
            return ':('

    first_name = models.CharField(max_length=200, default='Unknown')
    last_name = models.CharField(max_length=200, name='surname')
    visit_date = models.DateTimeField(default=datetime.now())