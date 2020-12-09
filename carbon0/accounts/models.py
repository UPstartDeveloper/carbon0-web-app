from django.db import models
from carbon0 import settings
from django.urls import reverse
from django.conf import settings

from carbon_quiz.models.mission import Mission
from carbon_quiz.models.question import Question


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mugshot = models.ImageField(
        upload_to="images/", null=True, blank=True, help_text="User profile image"
    )
    phone = models.CharField(max_length=20, null=True, blank=True)
    users_footprint = models.FloatField(
        default=0,
        help_text="The total carbon footprint of the User across all quizzes.",
    )
    offsets_level = models.IntegerField(
        default=0,
        choices=Mission.PRIORITIES,
        help_text=(
            "Which level of Airlines-Utilities Missions to recommend"
            + " for this player."
        ),
    )
    diet_level = models.IntegerField(
        default=0,
        choices=Mission.PRIORITIES,
        help_text=("Which level of Diet Missions to recommend" + " for this player."),
    )
    transit_level = models.IntegerField(
        default=0,
        choices=Mission.PRIORITIES,
        help_text=(
            "Which level of Transit Missions to recommend" + " for this player."
        ),
    )
    recycling_level = models.IntegerField(
        default=0,
        choices=Mission.PRIORITIES,
        help_text=(
            "Which level of Recycling Missions to recommend" + " for this player."
        ),
    )
    utilities_level = models.IntegerField(
        default=0,
        choices=Mission.PRIORITIES,
        help_text=(
            "Which level of Utilities Missions to recommend" + " for this player."
        ),
    )

    def __str__(self):
        """Return the related User's username."""
        return f"{self.user.username}'s Profile"

    def get_absolute_url(self):
        """Returns a fully qualified path for user profile."""
        pass

    def increase_user_footprint(self, quiz):
        """When a Quiz is completed, add the total carbon value
        to the User's profile.

        Parameters:
        quiz(Quiz): the Quiz which the user has just finished

        Returns: None

        """
        # add by the half, because this function is called twice
        self.users_footprint += quiz.carbon_value_total / 2
        self.save()
        return None

    def get_player_level(self, category):
        """
        Return the Profile's current level for a certain Question category.
        """
        # make a dict of all the Question categories and the profile's levels
        levels = [
            self.diet_level,
            self.transit_level,
            self.recycling_level,
            self.offsets_level,
            self.utilities_level,
        ]
        # get a list of the category abbreivations
        categories = [abbreviation for abbreviation, full in Question.CATEGORIES]
        category_level = dict(zip(categories, levels))
        # return the level value for the given category parameter
        return category_level[category]

    def change_level(self, category, lower_threshold, higher_threshold):
        """
        Update the Profile's current level for a certain Question category.

        Parameters:
        category(str): one of the 5 Question Categories
        lower_threshold(float): the value at which the profile's level
                                decrements 
        higher_threshold(float): the value at which the profile's level
                                 increases

        Returns: None
        """
        # see if the level needs to change, based on current footprint
        increase = None
        if self.users_footprint < lower_threshold:
            # we need to decrement the players level
            increase = False
        elif self.users_footprint > higher_threshold:
            # we need to increase the player's level
            increase = True
        # list the profile's levels, order corresponds to Question categories
        levels = [
            self.diet_level,
            self.transit_level,
            self.recycling_level,
            self.offsets_level,
            self.utilities_level,
        ]
        # iterate over the categories until we hit a match
        for index, question_category in Question.CATEGORIES:
            if category == question_category:
                # change the level in that category if possible
                if levels[index] < 3 and increase is True:
                    levels[index] += 1
                elif levels[index] > 0 and increase is False:
                    levels[index] -= 1
                # save and exit the function
                self.save()
                return None
