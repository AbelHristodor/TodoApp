from django.db import models
import datetime

# Create your models here.

class Todo(models.Model):
    details = models.CharField(max_length=250)
    due_date = models.DateField()
    created_date = models.DateField(default=datetime.datetime.today)

    def publish(self):
        self.created_date = datetime.datetime.today
        self.save()

    def __str__(self):
        return self.details