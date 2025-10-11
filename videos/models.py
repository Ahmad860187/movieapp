from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Video(models.Model):
    movie_id = models.AutoField(primary_key=True)
    movie_title = models.CharField(max_length=200)
    actor1_name = models.CharField(max_length=120)
    actor2_name = models.CharField(max_length=120, blank=True)
    director_name = models.CharField(max_length=120)

    GENRE_CHOICES = [
        ("COMEDY", "Comedy"),
        ("ROMANCE", "Romance"),
        ("ACTION", "Action"),
        ("DRAMA", "Drama"),
        ("HORROR", "Horror"),
        ("SCIFI", "Sci-Fi"),
        ("OTHER", "Other"),
    ]
    movie_genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    release_year = models.IntegerField(
        validators=[MinValueValidator(1888), MaxValueValidator(2100)]
    )

    def __str__(self):
        return f"{self.movie_title} ({self.release_year})"
