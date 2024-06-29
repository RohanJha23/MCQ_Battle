# Generated by Django 5.0.6 on 2024-06-29 11:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('body', models.TextField()),
                ('explanation', models.TextField()),
                ('options', models.JSONField()),
            ],
        ),
    ]
