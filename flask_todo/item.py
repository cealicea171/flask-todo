import datetime

class Task(object):
    def __init__(self, task, completed, datetime):
        self.task = task
        #the text of the actual to-do item.
        self.completed = False
        #A boolean marking the item as completed or not.
        self.datetime = datetime.datetime.now()
        # timestamp
