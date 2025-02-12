from django.db import models

# Create your models here.

# This line creates a class Task that inherits from models.Model, making it a Django model. 
# A model in Django is a Python class that maps to a database table.
class Task(models.Model):
    title       = models.CharField(max_length=200)        # This line creates a CharField named title with a maximum length of 200 characters.
    description = models.TextField(blank=True)            # This line creates a TextField named description that can be left blank.
    completed   = models.BooleanField(default=False)      # This line creates a BooleanField named completed with a default value of False.
    created_at  = models.DateTimeField(auto_now_add=True) # This line creates a DateTimeField named created_at that is automatically set when a Task instance is created.
    updated_at  = models.DateTimeField(auto_now=True)     # This line creates a DateTimeField named updated_at that is automatically set when a Task instance is updated.

    # This method returns the title of the task when the Task instance is printed or represented as a string.
    def __str__(self):
        return self.title           # This line returns the title of the Task instance.