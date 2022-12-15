import json
from django.db import transaction
from core.models import Exercise, Serie, Session, Training

def create_service(data: dict) -> dict:
    with transaction.atomic():
        trainings = json.loads(data["trainings"])
        session = Session.objects.create(
            name=data["session_name"],
            day_of_week=data["day_of_week"]
        )

        for training_data in trainings:
            exercise = Exercise.objects.get(pk=training_data["exercise"]["id"])
            training = Training.objects.create(
                session=session,
                exercise=exercise,
                series_qtd=training_data["qtd_series"],
                min_reps=training_data["min_reps"],
                max_reps=training_data["max_reps"],
            )
            series = training_data["series"]
            for serie in series:
                Serie.objects.create(
                    training=training,
                    load=serie["load"],
                    repetitions=serie["reps"],
                    order=serie["order"],
                    active=True,
                )

    return {
        "name": session.name,
        "day_of_week": session.day_of_week,
        "trainings": [{
            "exercise": training.exercise.name,
            "qtd_series": training.series_qtd,
            "min_reps": training.min_reps,
            "max_reps": training.max_reps,
        } for training in session.training_set.all()]
    }


def list_exercises():
    exercises = Exercise.objects.select_related('muscle_group').all()
    exercise_list = []

    for exercise in exercises:
        exercise_list.append({
            'id': exercise.id,
            'name': exercise.name,
            'min': exercise.muscle_group.min_reps,
            'max': exercise.muscle_group.max_reps,
        })

    return exercise_list


def list_sessions():
    sessions = Session.objects.prefetch_related("training_set", "training_set__exercise").all()        
    return [{
        "name": session.name,
        "day_of_week": session.day_of_week,
        "trainings": [{
            "exercise": training.exercise.name,
            "qtd_series": training.series_qtd,
            "min_reps": training.min_reps,
            "max_reps": training.max_reps,
        } for training in session.training_set.all()]
    } for session in sessions]
