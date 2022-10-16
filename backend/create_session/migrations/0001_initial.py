# Generated by Django 4.1.1 on 2022-09-24 23:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Exercise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("created_in", models.DateTimeField(auto_now_add=True)),
                ("updated_in", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="MuscleGroup",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                ("mrv", models.PositiveIntegerField(default=0)),
                ("mav", models.PositiveIntegerField(default=0)),
                ("mev", models.PositiveIntegerField(default=0)),
                ("min", models.PositiveIntegerField(default=0)),
                ("max", models.PositiveIntegerField(default=0)),
                ("created_in", models.DateTimeField(auto_now_add=True)),
                ("updated_in", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
                (
                    "day_of_week",
                    models.IntegerField(
                        choices=[
                            (1, "Sunday"),
                            (2, "Monday"),
                            (3, "Tuesday"),
                            (4, "Wednesday"),
                            (5, "Thursday"),
                            (6, "Friday"),
                            (7, "Saturday"),
                        ]
                    ),
                ),
                ("created_in", models.DateTimeField(auto_now_add=True)),
                ("updated_in", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Training",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("series_qtd", models.PositiveIntegerField(default=0)),
                ("min", models.PositiveIntegerField(default=0)),
                ("max", models.PositiveIntegerField(default=10)),
                ("created_in", models.DateTimeField(auto_now_add=True)),
                ("updated_in", models.DateTimeField(auto_now=True)),
                (
                    "exercise",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="create_session.exercise",
                    ),
                ),
                (
                    "session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="create_session.session",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Serie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "load",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                ("repetitions", models.PositiveIntegerField(default=0)),
                ("order", models.PositiveIntegerField()),
                ("active", models.BooleanField()),
                (
                    "active_since",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("created_in", models.DateTimeField(auto_now_add=True)),
                ("updated_in", models.DateTimeField(auto_now=True)),
                (
                    "training",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="create_session.training",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="exercise",
            name="muscle_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="create_session.musclegroup",
            ),
        ),
    ]
