# Generated by Django 4.1.7 on 2023-04-02 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Database_Fundamentals', models.IntegerField()),
                ('Computer_Architecture', models.IntegerField()),
                ('Distributed_Computing', models.IntegerField()),
                ('Cyber_Security', models.IntegerField()),
                ('Networking', models.IntegerField()),
                ('Development', models.IntegerField()),
                ('Programming_Skills', models.IntegerField()),
                ('Project_Management', models.IntegerField()),
                ('Computer_Forensics', models.IntegerField()),
                ('Technical_Communication', models.IntegerField()),
                ('AI_ML', models.IntegerField()),
                ('Software_Engineering', models.IntegerField()),
                ('Business_Analysis', models.IntegerField()),
                ('Communication_skills', models.IntegerField()),
                ('Data_Science', models.IntegerField()),
                ('Troubleshooting_skills', models.IntegerField()),
                ('Graphics_Designing', models.IntegerField()),
                ('Openness', models.IntegerField()),
                ('Conscientiousness', models.IntegerField()),
                ('Extraversion', models.IntegerField()),
                ('Agreeableness', models.IntegerField()),
                ('Emotional_Range', models.IntegerField()),
                ('Conversation', models.IntegerField()),
                ('Openness_Change', models.IntegerField()),
                ('Hedonism', models.IntegerField()),
                ('Self_enhancement', models.IntegerField()),
                ('Self_transcendence', models.IntegerField()),
            ],
        ),
    ]
