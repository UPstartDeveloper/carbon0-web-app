import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class Question(models.Model):
    '''Represents a single question on the Carbon calculator quiz.'''
    question_text = models.CharField(max_length=500,
        help_text="Question for the user"
    )
    question_info = models.TextField(
        help_text="Explains any vocabulary relevant to the question."
    )
    carbon_value = models.FloatField(
        help_text="Tons of carbon that may be present in user's footprint."
    )
    # Define the categories a question can fall into
    CATEGORIES = [
        ('D', 'Diet'),
        ('T', 'Transit'),
        ('R', 'Recycling'),
        ('A', 'Airline-Travel'),
        ('U', 'Utilities'),
    ]
    category = models.CharField(max_length=1, choices=CATEGORIES,
        help_text="The area of sustainability to which this question relates."
    )
    learn_more_link = models.CharField(max_length=1000, help_text=
        "Hyperlink where the user can learn more about the question",
        null=True, blank=True
    )

    def __str__(self):
        '''Returns the category of the Question, and it's id.'''
        return f'Question {self.category} {self.id}'


class Quiz(models.Model):
    '''Represents a collection of 5 questions given to the user.'''
    title = models.CharField(max_length=500,
                             unique=True,
                             help_text="Title of the quiz.",
                             null=True)
    slug = models.CharField(max_length=500,
                            blank=True, editable=False,
                            help_text=("Unique URL path to access this quiz. "
                                       + "Generated by the system."))
    questions = ArrayField(
        models.IntegerField(), size=5, 
        help_text="Array of ids for the quiz questions.", null=True, blank=True
    )
    active_question = models.IntegerField(
        help_text="Id of the question currently being asked.", 
        default=0, blank=True
    )
    carbon_value_total = models.FloatField(
        blank=True, default=0, 
        help_text='Total metric tons of carbon that the user can eliminate.'
    )

    def __str__(self):
        '''Returns human-readable name of the Quiz.'''
        return f'{self.title}'
    

class Mission(models.Model):
    '''Represents a possible action the user takes to help the environment.'''
    title = models.CharField(max_length=500,
                             unique=True,
                             help_text="Title of the mission.",
                             null=True)
    description = models.TextField(
        help_text="Explains the details of the mission.",
        null=True, blank=True
    )
    learn_more = models.TextField(
        help_text="Explains why the mission matters.",
        null=True, blank=True
    )
    status = models.BooleanField(
        default=False,
        help_text="If the mission is done or not.")
    links = ArrayField(
        models.CharField(max_length=500), size=3,
        help_text="Links that the user can click to complete the mission.",
        null=True, blank=True
    )
    question = models.ForeignKey(
        Question, on_delete=models.PROTECT,
        help_text="The question to which this mission relates.",
        null=True  # can be null to start, question should be populated later
    )

    def __str__(self):
        '''Returns human-readable name of the Mission.'''
        return f'{self.title}'


class Achievement(models.Model):
    completion_date = models.DateTimeField(
        help_text="Date mission was accomplished",
        null=True, blank=True                                
    )
