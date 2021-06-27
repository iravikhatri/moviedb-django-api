# Generated by Django 2.2 on 2021-06-26 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('imdb_score', models.IntegerField()),
                ('popularity', models.IntegerField()),
                ('director', models.CharField(max_length=64)),
                ('genres', models.ManyToManyField(blank=True, related_name='genres', to='movies.Genre')),
            ],
        ),
    ]
