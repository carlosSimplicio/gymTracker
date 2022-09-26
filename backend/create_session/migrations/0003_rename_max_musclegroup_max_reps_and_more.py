# Generated by Django 4.1.1 on 2022-09-25 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("create_session", "0002_rename_created_in_exercise_created_at_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="musclegroup",
            old_name="max",
            new_name="max_reps",
        ),
        migrations.RenameField(
            model_name="musclegroup",
            old_name="min",
            new_name="min_reps",
        ),
        migrations.RenameField(
            model_name="training",
            old_name="max",
            new_name="max_reps",
        ),
        migrations.RenameField(
            model_name="training",
            old_name="min",
            new_name="min_reps",
        ),
    ]