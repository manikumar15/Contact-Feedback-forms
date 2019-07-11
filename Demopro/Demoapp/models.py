from django.db import models
from multiselectfield import MultiSelectField

#FEEDBACK MODEL:
class FeedbackData(models.Model):
    
    name=models.CharField(max_length=50)
    rating=models.IntegerField()
    date=models.DateTimeField()
    feedback=models.TextField(max_length=300)
    

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

#CONTACT MODEL:
class ContactData(models.Model):
    
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=300)
    mobile=models.BigIntegerField()

    COURSES_CHOICE = (('python','Python'),
        			('django','Django'),
        			('html','HTML'),
        			('css','CSS'))
    courses=MultiSelectField(max_length=300,choices=COURSES_CHOICE)

    SHIFT_CHOICE = (('morning','Morning'),
        ('evening','Evening'),
        ('afternoon','Afternoon'),
        ('nght','Night'))
    shift=MultiSelectField(max_length=200,choices=SHIFT_CHOICE)

    LOCATION_CHOICE = (('hyderabad','Hyderabad'),
        ('bangalore','Bangalore'),
        ('chennai','Chennai'),
        ('pune','Pune'))
    location=MultiSelectField(max_length=20,choices=LOCATION_CHOICE)

    gender=models.CharField(max_length=10)
    date=models.DateField(max_length=100)

   
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

#COURSES MODEL:
class CoursesData(models.Model):
    
    course_id=models.IntegerField()
    course_name=models.CharField(max_length=20)
    course_duration=models.CharField(max_length=20)
    course_fee=models.IntegerField()
    start_date=models.DateTimeField()
    start_time=models.DateTimeField()
    trainer_name=models.CharField(max_length=20)
    trainer_experience=models.CharField(max_length=20)
    

    def __unicode__(self):
        return self.course_name

    def __str__(self):
        return self.course_name

