# Generated by Django 5.0.1 on 2024-01-21 18:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catigory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjects', models.CharField(choices=[('sport', 'sport'), ('game', 'game'), ('animals', 'animals'), ('food', 'food'), ('coding', 'coding')], max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text_post', models.TextField()),
                ('content_post', models.CharField(max_length=20)),
                ('time_post', models.DateTimeField(auto_now_add=True)),
                ('raiting_post', models.IntegerField(default=0)),
                ('profil_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModalsDateBase.author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_comment', models.TextField(max_length=100)),
                ('data_time_comment', models.DateTimeField(auto_now_add=True)),
                ('rating_comment', models.IntegerField(default=0)),
                ('user_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModalsDateBase.post')),
            ],
        ),
        migrations.CreateModel(
            name='PostCatigory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conect_catigory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModalsDateBase.catigory')),
                ('conect_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ModalsDateBase.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='catigory_post',
            field=models.ManyToManyField(through='ModalsDateBase.PostCatigory', to='ModalsDateBase.catigory'),
        ),
    ]