# Generated by Django 3.1.4 on 2020-12-05 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superhero', '0003_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='superhero',
            name='about',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
