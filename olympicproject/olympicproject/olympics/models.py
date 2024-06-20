# olympics/models.py

#from django import models
from django.db import models

class OlympicHost(models.Model):
    game_slug = models.CharField(max_length=255)
    game_end_date = models.DateTimeField()
    game_start_date = models.DateTimeField()
    game_location = models.CharField(max_length=255)
    game_name = models.CharField(max_length=255)
    game_season = models.CharField(max_length=50)
    game_year = models.IntegerField()

    def __str__(self):
        return f"{self.game_name} ({self.game_year})"
    
class OlympicAthlete(models.Model):
    athlete_url = models.URLField(max_length=500)
    athlete_full_name = models.CharField(max_length=255)
    games_participations = models.IntegerField()
    first_game = models.CharField(max_length=255)
    athlete_year_birth = models.CharField(max_length=10)
    athlete_medals = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.athlete_full_name

class OlympicMedal(models.Model):
    discipline_title = models.CharField(max_length=255)
    slug_game = models.CharField(max_length=255)
    event_title = models.CharField(max_length=255)
    event_gender = models.CharField(max_length=50)
    medal_type = models.CharField(max_length=50)
    participant_type = models.CharField(max_length=50)
    participant_title = models.CharField(max_length=255)
    athlete_url = models.URLField(max_length=500)
    athlete_full_name = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=10)
    country_3_letter_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.athlete_full_name} - {self.medal_type} ({self.slug_game})"

class OlympicResult(models.Model):
    discipline_title = models.CharField(max_length=255)
    event_title = models.CharField(max_length=255)
    slug_game = models.CharField(max_length=100)
    participant_type = models.CharField(max_length=50)
    medal_type = models.CharField(max_length=10, null=True, blank=True)
    athletes = models.TextField()
    rank_equal = models.BooleanField()
    rank_position = models.IntegerField()
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)
    country_3_letter_code = models.CharField(max_length=3)
    athlete_url = models.URLField(null=True, blank=True)
    athlete_full_name = models.CharField(max_length=255, null=True, blank=True)
    value_unit = models.CharField(max_length=50, null=True, blank=True)
    value_type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.discipline_title} - {self.event_title} ({self.slug_game})"
