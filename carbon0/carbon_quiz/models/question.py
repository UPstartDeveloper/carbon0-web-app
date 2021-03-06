import os

from django.conf import settings
from django.db import models


class Question(models.Model):
    """Represents a single question on the Carbon calculator quiz."""

    question_text = models.CharField(max_length=500, help_text="Question for the user")
    question_info = models.TextField(
        help_text="Explains any vocabulary relevant to the question."
    )
    carbon_value = models.FloatField(
        help_text="Tons of carbon that may be present in user's footprint."
    )
    # Define the categories a question can fall into
    CATEGORIES = [
        ("D", "Diet"),
        ("T", "Transit"),
        ("R", "Recycling"),
        ("A", "Airline-Travel"),
        ("U", "Utilities"),
    ]
    category = models.CharField(
        max_length=1,
        choices=CATEGORIES,
        help_text="The area of sustainability to which this question relates.",
    )
    learn_more_link = models.CharField(
        max_length=1000,
        help_text="Hyperlink where the user can learn more about the question",
        null=True,
        blank=True,
    )
    # save static files related to this model in app subdirectory
    UPLOAD_LOCATION = os.path.join("carbon_quiz", "static", "carbon_quiz", "images")
    learn_image = models.ImageField(
        upload_to=UPLOAD_LOCATION,
        null=True,
        blank=True,
        help_text="Symbolizes what user needs to work on.",
    )
    ANSWERS = [(1, "Yes"), (0, "No"), (-1, "Open-Response")]
    improvement_response = models.IntegerField(
        choices=ANSWERS,
        default=0,
        help_text=(
            "Response that says the user needs to improve, with regards "
            + "to this area of their carbon footprint."
        ),
    )
    is_quiz_question = models.BooleanField(
        default=True, help_text="Will the question appear on a Quiz at all."
    )

    def __str__(self):
        """Returns the category of the Question, and it's id."""
        return f"Question {self.category} {self.id}"

    @classmethod
    def get_category_abbreviations(cls):
        """Returns a list of just abbreviations for Question categories."""
        categories = [
            category_abbreviation
            for category_abbreviation, full_name in Question.CATEGORIES
        ]
        return categories

    @classmethod
    def get_category_fullnames(cls):
        """Returns a list of just abbreviations for Question categories."""
        categories = [
            full_name for category_abbreviation, full_name in Question.CATEGORIES
        ]
        return categories
