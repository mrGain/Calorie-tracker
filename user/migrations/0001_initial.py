# Generated by Django 4.1.4 on 2022-12-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('target_calorie_intake', models.IntegerField()),
                ('total_calorie_intake', models.IntegerField()),
                ('achived_calorie_intake', models.BooleanField()),
                ('target_calorie_burn', models.IntegerField()),
                ('total_calorie_burn', models.IntegerField()),
                ('achived_calorie_burn', models.BooleanField()),
            ],
        ),
    ]
