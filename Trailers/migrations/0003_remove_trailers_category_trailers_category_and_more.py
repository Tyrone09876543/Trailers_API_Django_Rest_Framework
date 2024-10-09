# Generated by Django 4.0.6 on 2022-08-03 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trailers', '0002_trailers_cast_trailers_description_trailers_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trailers',
            name='category',
        ),
        migrations.AddField(
            model_name='trailers',
            name='category',
            field=models.ManyToManyField(blank=True, to='Trailers.category'),
        ),
        migrations.AlterField(
            model_name='trailers',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]