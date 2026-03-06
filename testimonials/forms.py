from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ["name", "quote", "rating", "is_published"]
        widgets = {
            "quote": forms.Textarea(attrs={"rows": 4}),
        }