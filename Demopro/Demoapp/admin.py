from django.contrib import admin
from .models import FeedbackData,ContactData,CoursesData

admin.site.site_header = 'Mani Kumar'

#FEEDBACK ADMIN:
class Feedbackadmin(admin.ModelAdmin):
    list_display = ('name','rating','date','feedback')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(FeedbackData,Feedbackadmin)


#CONTACT ADMIN:
class Contactadmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','courses','shift','location','gender','date')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(ContactData,Contactadmin)

#COURSES ADMIN:
class Coursesadmin(admin.ModelAdmin):
    list_display = ('course_id','course_name','course_duration','course_fee','start_date','start_time','trainer_name','trainer_experience')
    list_filter = ('course_name',)
    search_fields = ('course_name',)

admin.site.register(CoursesData,Coursesadmin)