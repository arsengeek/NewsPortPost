# Generated by Django 5.0.1 on 2024-02-24 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModalsDateBase', '0008_alter_post_author_remove_post_content_post_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ModalsDateBase.author'),
        ),
    ]
