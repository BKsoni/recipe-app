# Generated by Django 4.2.3 on 2023-07-27 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vege", "0003_recipe_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe", name="views", field=models.IntegerField(default=0),
        ),
    ]
