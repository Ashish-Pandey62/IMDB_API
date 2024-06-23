# Generated by Django 4.2.12 on 2024-06-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("watchlist_app", "0006_review_review_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="watchlist",
            name="avg_rating",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="watchlist",
            name="number_rating",
            field=models.IntegerField(default=0),
        ),
    ]
