from django.db import models
from embed_video.fields import EmbedVideoField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CheckConstraint, Q


GENRE_CHOICES = (
    ("ACT", "Action"),
    ("ADV", "Adventure"),
    ("COM", "Comedy"),
    ("DRA", "Drama"),
    ("FAN", "Fantasy"),
    ("HIS", "Historical"),
    ("HOR", "Horror"),
    ("ROM", "Romance"),
    ("SCI", "Science Fiction"),
    ("THR", "Thriller"),
    ("WES", "Western"),
    ("OTH", "Other")
)


class Genre(models.Model):
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES)

    def __str__(self):
        return f"{self.genre}"


class Video(models.Model):
    title = models.CharField(max_length=150)
    url = EmbedVideoField()
    imdb_url = models.URLField(verbose_name='imdb', null=True)
    added = models.DateTimeField(auto_now_add=True)
    year = models.PositiveSmallIntegerField()
    rating = models.FloatField(null=True, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)],)
    cover = models.ImageField(upload_to='static/img')
    genre = models.ManyToManyField(Genre, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.title}, {self.year}'

    @property
    def img(self):
        try:
            url = self.cover.url
        except:
            url = 'img/placeholder.png'
        return url

    class Meta:
        ordering = ['-added']
        constraints = (CheckConstraint(check=Q(rating__gte=0.0) & Q(rating__lte=10.0), name='Video_rating_range'),)

