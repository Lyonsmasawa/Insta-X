# Generated by Django 4.0.3 on 2022-04-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0012_remove_image_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(to='insta.tag'),
        ),
    ]