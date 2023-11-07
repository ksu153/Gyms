# Generated by Django 4.2.6 on 2023-10-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(choices=[('Bodyweight Cardio', 'odyweight Cardio'), ('Bodyweight Core', 'Bodyweight Core'), ('Beginner HIIT', 'Beginner HIIT'), ('Total Body Strength', 'Total Body Strength')], default='Group Classes', max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(choices=[('3 PM', '3 PM'), ('3:30 PM', '3:30 PM'), ('4 PM', '4 PM'), ('4:30 PM', '4:30 PM'), ('5 PM', '5 PM'), ('5:30 PM', '5:30 PM')], default='3 PM', max_length=10),
        ),
    ]
