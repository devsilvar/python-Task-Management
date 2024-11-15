from django.db import models
import datetime 

# Create your models here.

def one_hour_ago():
    return datetime.datetime.now() - datetime.timedelta(hours=1)

class todo(models.Model):
    class Category(models.TextChoices):
        WORK = "Work"
        CHORES = "Chores"
        LEISUIRE = "Leisures"
        TRAVEL = "Travel"
        ALL = "All"

    todo_name = models.CharField(max_length=200)
    todo_desc = models.TextField()
    todo_category = models.CharField(max_length=8 , choices=Category.choices , default=Category.ALL)
    time_created = models.DateTimeField(default=datetime.datetime.now(), editable=True)
    todo_status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.todo_name



