# Generated by Django 5.0.1 on 2024-02-03 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModalsDateBase', '0005_alter_catigory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catigory',
            name='category',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]