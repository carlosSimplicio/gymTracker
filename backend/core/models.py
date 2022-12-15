from django.db import models
from django.utils import timezone


class Session(models.Model):
    class DaysOfWeek(models.IntegerChoices):
        SUNDAY = 1, "Sunday"
        MONDAY = 2, "Monday"
        TUESDAY = 3, "Tuesday"
        WEDNESDAY = 4, "Wednesday"
        THURSDAY = 5, "Thursday"
        FRIDAY = 6, "Friday"
        SATURDAY = 7, "Saturday"

    __empty__ = "(Unknown)"

    name = models.CharField(max_length=256)
    day_of_week = models.IntegerField(choices=DaysOfWeek.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MuscleGroup(models.Model):
    name = models.CharField(max_length=256)
    mrv = models.PositiveIntegerField(default=0) # Maximum recovery volume (Series/week)
    mav = models.PositiveIntegerField(default=0) # Maximum adaptive volume (Series/week)
    mev = models.PositiveIntegerField(default=0) # Mininum effective volume (Series/week)
    min_reps = models.PositiveIntegerField(default=0)
    max_reps = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Exercise(models.Model):
    name = models.CharField(max_length=256)
    muscle_group = models.ForeignKey(MuscleGroup, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Training(models.Model):
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    series_qtd = models.PositiveIntegerField(default=0)
    min_reps = models.PositiveIntegerField(default=0)
    max_reps = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Serie(models.Model):
    training = models.ForeignKey(Training, on_delete=models.PROTECT)
    load = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    repetitions = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField()
    active = models.BooleanField()
    active_since = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
