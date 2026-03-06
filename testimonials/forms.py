from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ["quote", "rating"]
        widgets = {
            "quote": forms.Textarea(attrs={"rows": 4}),
        }