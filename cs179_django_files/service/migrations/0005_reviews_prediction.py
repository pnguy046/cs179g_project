# Generated by Django 2.0.5 on 2018-12-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_remove_reviews_prediction'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='prediction',
            field=models.CharField(default='0', max_length=3),
        ),
    ]