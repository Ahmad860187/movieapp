from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ["movie_title","actor1_name","actor2_name","director_name","movie_genre","release_year"]
        widgets = {
            "movie_title": forms.TextInput(attrs={"placeholder": "e.g. The Matrix"}),
            "actor1_name": forms.TextInput(attrs={"placeholder": "Lead actor"}),
            "actor2_name": forms.TextInput(attrs={"placeholder": "Second actor"}),
            "director_name": forms.TextInput(attrs={"placeholder": "Director"}),
            "movie_genre": forms.Select(),
            "release_year": forms.NumberInput(attrs={"min": 1888, "max": 2100}),
        }
        labels = {
            "movie_title": "Title",
            "actor1_name": "Actor 1",
            "actor2_name": "Actor 2",
            "director_name": "Director",
            "movie_genre": "Genre",
            "release_year": "Year",
        }
