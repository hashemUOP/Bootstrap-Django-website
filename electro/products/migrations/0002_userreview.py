# Generated by Django 5.0.6 on 2024-11-04 19:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserReview',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('star_reviews', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('review', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
