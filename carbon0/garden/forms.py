from django import forms
from .models.leaf import Leaf
from .models.plant import Plant


class LeafForm(forms.ModelForm):
    """A form for uploading leaf images."""

    class Meta:
        model = Leaf
        fields = ["image"]


class PlantForm(forms.ModelForm):
    """A form for adding new Plant models."""

    class Meta:
        model = Plant
        fields = [
            "nickname",
            "common_name",
            "is_edible",
            "description",
        ]


class HarvestForm(forms.Form):
    """A form for the user to record the amount of produce they grew."""
    UNITS = [
        ("kg", "Kilograms"),
        ("lbs", "English Pounds")
    ]
    measuring_unit = forms.ChoiceField(
        choices=UNITS, 
        help_text="The unit the gardener measures produce in."
    )
    amount_harvested = forms.FloatField(
        help_text="How much produce did you harvest this \
        season from your garden (in pounds)?"
    )
