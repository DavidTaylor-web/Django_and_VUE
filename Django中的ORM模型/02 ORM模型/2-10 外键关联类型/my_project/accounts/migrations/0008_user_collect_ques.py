# Generated by Django 3.0.5 on 2020-05-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_answer_classify_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='collect_ques',
            field=models.ManyToManyField(to='accounts.Question'),
        ),
    ]
