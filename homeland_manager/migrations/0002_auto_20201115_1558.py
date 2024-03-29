# Generated by Django 3.1.1 on 2020-11-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeland_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='common_due',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='apartment',
            name='elevator_due',
            field=models.FloatField(max_length=5),
        ),
        migrations.AlterField(
            model_name='commondue',
            name='other_comment',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='commondue',
            name='other_payments',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='commondue',
            name='stairs_electricity',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='elevatordue',
            name='elevator_additional',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='elevatordue',
            name='elevator_comment',
            field=models.FloatField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='elevatordue',
            name='elevator_electricity',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='monthlydue',
            name='monthly_common',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='monthlydue',
            name='monthly_elevator',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='monthlydue',
            name='monthly_given',
            field=models.FloatField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='monthlydue',
            name='status',
            field=models.FloatField(blank=True, choices=[('a', 'Awaiting for payment'), ('m', 'Missed payment'), ('p', 'Payed'), ('s', 'Skip')], default='a', help_text='monthly bills information', max_length=1),
        ),
        migrations.AlterField(
            model_name='owner',
            name='names',
            field=models.FloatField(max_length=30),
        ),
    ]
