# Generated by Django 2.0.1 on 2019-06-03 18:30

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=300)),
                ('mobile', models.BigIntegerField()),
                ('courses', multiselectfield.db.fields.MultiSelectField(choices=[('python', 'Python'), ('django', 'Django'), ('html', 'HTML'), ('css', 'CSS')], max_length=300)),
                ('shift', multiselectfield.db.fields.MultiSelectField(choices=[('morning', 'Morning'), ('evening', 'Evening'), ('afternoon', 'Afternoon'), ('nght', 'Night')], max_length=200)),
                ('location', multiselectfield.db.fields.MultiSelectField(choices=[('hyderabad', 'Hyderabad'), ('bangalore', 'Bangalore'), ('chennai', 'Chennai'), ('pune', 'Pune')], max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('date', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CoursesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('course_name', models.CharField(max_length=20)),
                ('course_duration', models.CharField(max_length=20)),
                ('course_fee', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('start_time', models.DateTimeField()),
                ('trainer_name', models.CharField(max_length=20)),
                ('trainer_experience', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('feedback', models.TextField(max_length=300)),
            ],
        ),
    ]
