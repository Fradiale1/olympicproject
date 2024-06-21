# olympics/models.py

#from django import models
import uuid
from django.db import models

class Host(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game_slug = models.CharField(max_length=100)
    game_end_date = models.DateTimeField()
    game_start_date = models.DateTimeField()
    game_location = models.CharField(max_length=255)
    game_name = models.CharField(max_length=255)
    game_season = models.CharField(max_length=100)
    game_year = models.IntegerField()

    def __str__(self):
        return self.game_name

class Athlete(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    athlete_url = models.CharField(max_length=255)
    athlete_full_name = models.CharField(max_length=255)
    games_participations = models.IntegerField()
    first_game = models.CharField(max_length=100)
    athlete_year_birth = models.IntegerField()

    def __str__(self):
        return self.athlete_full_name


class Medal(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discipline_title = models.CharField(max_length=255)
    slug_game = models.CharField(max_length=100)
    event_title = models.CharField(max_length=255)
    event_gender = models.CharField(max_length=10)
    medal_type = models.CharField(max_length=50)
    participant_type = models.CharField(max_length=50)
    participant_title = models.CharField(max_length=255)
    athlete_url = models.CharField(max_length=255)
    athlete_full_name = models.CharField(max_length=255)
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3)
    country_3_letter_code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.medal_type} - {self.event_title}"

class Result(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discipline_title = models.CharField(max_length=255)
    event_title = models.CharField(max_length=255)
    slug_game = models.CharField(max_length=100)
    participant_type = models.CharField(max_length=50)
    medal_type = models.CharField(max_length=50)
    athletes = models.TextField()  # Considerando che 'athletes' è una stringa separata da virgola o simile
    rank_equal = models.BooleanField()
    rank_position = models.CharField(max_length=10)
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3)
    country_3_letter_code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.event_title} - {self.country_name}"
