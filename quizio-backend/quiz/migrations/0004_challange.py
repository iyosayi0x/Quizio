# Generated by Django 4.0.4 on 2022-06-22 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0003_alter_question_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challangee_score', models.IntegerField(default=0)),
                ('challanger_score', models.IntegerField(default=0)),
                ('quiz', models.JSONField()),
                ('accepted', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('expiry', models.DateTimeField()),
                ('challangee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challangee', to=settings.AUTH_USER_MODEL)),
                ('challanger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='challanger', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
