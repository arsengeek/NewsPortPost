# Generated by Django 5.0.1 on 2024-02-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModalsDateBase', '0007_remove_post_author_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ManyToManyField(default=None, related_name='posts', to='ModalsDateBase.catigory'),
        ),
        migrations.RemoveField(
            model_name='post',
            name='content_post',
        ),
        migrations.AddField(
            model_name='post',
            name='content_post',
            field=models.ManyToManyField(to='ModalsDateBase.catigory'),
        ),
    ]