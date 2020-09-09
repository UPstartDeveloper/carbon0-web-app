import random

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView)

from .models import (
    Achievement,
    Mission,
    Question,
    Quiz,
)


class QuizCreate(CreateView):
    '''View to create new Quiz instance from randomly picked questions.'''
    model = Quiz
    fields = []
    template_name = 'carbon_quiz/quiz/create.html'
    queryset = Question.objects.all()

    def generate_random_question(self, category):
        '''Gets a Question model in a specific category randomly.'''
        category_questions = Question.objects.filter(category=category)
        return random.sample(category_questions, 1)

    def form_valid(self, form):
        '''Initializes the Questions the user will answer on the Quiz.'''
        # get random questions
        quiz_questions = list()
        for category in Question.CATEGORIES:
            # get the value stored for the category field on the model
            category_value, category_full_name = category
            # get a Question instance in that category
            next_question = self.generate_random_question(category_value)
            # add the id of the Question to the list
            quiz_questions.append(next_question.id)
        # set the questions list on the model
        form.instance.questions = quiz_questions
        return super().form_valid(form)


class QuizDetail(DetailView):
    '''Displays questions on the quiz to answer, or the missions to complete.'''
    model = Question
    template_name = 'carbon_quiz/quiz/detail.html'

    def get(self, request, slug, question_answered=0):
        """
        Renders a page to show the question currently being asked.
       
        Parameters:
        request(HttpRequest): the GET request sent to the server
        slug(slug): unique slug value of the Quiz instance
        question_answered(int): the id field of the question,
                                passed in if the user answers yes
        
        Returns:
        HttpResponse: the view of the detail template
        
        """
        # get the Quiz instance 
        quiz = Quiz.object.get(slug=slug)
           # if the user just answered 'yes', then ignore the question
        if question_answered > 0:
            quiz.questions[quiz.active_question] = 0
        # set the context
        context = dict()
        # if the next question needs to be shown
        if quiz.active_question < 5:
            # get the question to display
            question_id = quiz.questions[quiz.active_question]
            question_obj = Question.objects.get(id=question_id)
            # increment the active_question for the next call
            quiz.active_question += 1
            # add key value pairs to the context
            context = {
                'quiz': quiz,
                'question': question_obj,
                'show_question': True  # tells us to display a Question
            }
        # otherwise show the mission start page
        else:  # quiz.active_question = 5
            # find the missions the user can choose
            missions = list()
            for question_id in quiz.questions:
                # check if this question was answered no (needs a mission)
                if question_id > 0:
                    # get the question
                    question_obj = Question.objects.get(id=question_id)
                    # get a random Mission related to the Question
                    related_missions = Mission.objects.filter(question=question_obj)
                    mission = random.sample(related_missions, 1)
                    # add to the list of Missions
                    missions.append(mission)
            # add key value pairs to the context
            context = {
                'quiz': quiz,
                'question': question_obj,
                'missions': missions,  # possible missions for the user 
                'show_question': False  # tells us to display Missions
            }
        # return the response
        return render(request, self.template_name, context)
    