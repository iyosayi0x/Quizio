# Generated by Django 4.0.4 on 2022-06-15 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='correct_option',
            field=models.CharField(choices=[('A', 'option_a'), ('B', 'option_b'), ('C', 'option_c'), ('D', 'option_d')], default=('A', 'option_a'), max_length=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='mode',
            field=models.CharField(choices=[('EASY', 'EASY'), ('BASIC', 'BASIC'), ('HARD', 'HARD')], default=('EASY', 'EASY'), max_length=40),
        ),
    ]