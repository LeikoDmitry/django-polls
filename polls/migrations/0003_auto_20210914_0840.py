# Generated by Django 3.1.7 on 2021-09-14 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_is open'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Is open',
            new_name='opened',
        ),
    ]
