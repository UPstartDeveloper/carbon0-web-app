from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response

from carbon_quiz.models.question import Question
from carbon_quiz.models.quiz import Quiz


# Create your views here.
class QuizUpdate(APIView):
    """
    Updates the questions that have been answered yes/no in the Quiz,
    and then moves to the next template.
    """
    def get(self, request, quiz_slug, question_response):
        """
        Uses the answer to the Question the user has just responded to,
        to update the array of questions related to a Quiz.

        Parameters:
        request(HttpRequest)
        quiz_slug(str): the unique slug value of one of the Quizzes
        question_response(int): 0 or 1, which means the user responded
                                   no or yes (respectively)

        Returns:
        HttpResponse: a view of the QuizDetail, with the next question, 
                      or missions for the user

        """
        # get the Quiz instance 
        quiz = Quiz.objects.get(slug=quiz_slug)
        # get the current Question 
        question_id = quiz.questions[quiz.active_question]
        question_obj = Question.objects.get(id=question_id)
        # if the user just answered 'yes', 
        if question_response == 1:
            # ignore the question later, when finding missions
            quiz.questions[quiz.active_question] = 0
        # if question was answered no
        elif question_response == 0 and quiz.active_question > 0:
            # increment the total carbon value so far
            quiz.increment_carbon_value(question_obj)
        # increment the active_question for the next call
        quiz.increment_active_question()
        # return a redirect view the next Question on the Quiz 
        path_components = {
            'slug': quiz_slug,
        }
        return HttpResponseRedirect(
            reverse('carbon_quiz:quiz_detail', kwargs=path_components)
        )
