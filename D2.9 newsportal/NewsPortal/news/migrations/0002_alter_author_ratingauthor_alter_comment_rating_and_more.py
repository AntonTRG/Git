# Generated by Django 4.0.1 on 2022-01-09 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='ratingAuthor',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.SmallIntegerField(default=0),
        ),
    ]
