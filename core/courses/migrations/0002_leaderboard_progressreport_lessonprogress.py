# Generated by Django 5.2.1 on 2025-06-06 12:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Leaderboard",
            fields=[
                ("leader_id", models.AutoField(primary_key=True, serialize=False)),
                ("score", models.IntegerField(default=0)),
                ("updated_at", models.DateField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProgressReport",
            fields=[
                ("report_id", models.AutoField(primary_key=True, serialize=False)),
                ("report_date", models.DateField(auto_now_add=True)),
                ("completed_lessons", models.IntegerField(default=0)),
                ("total_score", models.IntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LessonProgress",
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
                ("is_completed", models.BooleanField(default=False)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "lesson",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="courses.lesson"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "lesson")},
            },
        ),
    ]
