# Generated by Django 3.0.8 on 2020-09-08 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('educational_film', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='sds',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='has_titles', to='educational_film.Article'),
        ),
    ]