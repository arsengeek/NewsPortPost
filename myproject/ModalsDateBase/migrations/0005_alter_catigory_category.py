# Generated by Django 5.0.1 on 2024-02-03 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModalsDateBase', '0004_remove_catigory_subjects_remove_post_catigory_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catigory',
            name='category',
            field=models.CharField(default=2, max_length=50),
        ),
    ]
