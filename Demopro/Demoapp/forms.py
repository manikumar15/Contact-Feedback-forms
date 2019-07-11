from django import forms
from .models import FeedbackData,ContactData
from multiselectfield import MultiSelectFormField

#FEEDBACK FORM
class FeedbackForm(forms.Form):
    name=forms.CharField(
    	label="Enter your name :",
    	widget=forms.TextInput(

    		attrs={
    			'class':'form-control',
    			'placeholder':'Enter your name'
    		}

    	)
    )
    rating=forms.IntegerField(
    	label="Enter your rating :",
    	widget=forms.NumberInput(

    		attrs={
    			'class':'form-control',
    			'placeholder':'Enter your rating'
    		}

    	)
    )
    feedback=forms.CharField(
    	label="Enter your feedback :",
    	widget=forms.TextInput(

    		attrs={
    			'class':'form-control',
    			'placeholder':'Enter your feedback'
    		}

    	)
    )

#CONTACT FORM:
class ContactForm(forms.Form):
    name=forms.CharField(
        label="Enter your name :",
        widget=forms.TextInput(

            attrs={
                'class':'form-control',
                'placeholder':'Enter your name'
            }

        )
    )
    email=forms.CharField(
        label="Enter your email :",
        widget=forms.EmailInput(

            attrs={
                'class':'form-control',
                'placeholder':'Enter your email'
            }

        )
    )
    mobile=forms.IntegerField(
        label="Enter your mobile :",
        widget=forms.NumberInput(

            attrs={
                'class':'form-control',
                'placeholder':'Enter your mobile number'
            }

        )
    )
    COURSES_CHOICE = (
        ('python','Python'),
        ('django','Django'),
        ('html','HTML'),
        ('css','CSS')
    )
    courses=MultiSelectFormField(max_length=30,choices=COURSES_CHOICE)

    SHIFT_CHOICE = (
        ('morning','Morning'),
        ('evening','Evening'),
        ('afternoon','Afternoon'),
        ('nght','Night')
        
    )
    shift=MultiSelectFormField(max_length=30,choices=SHIFT_CHOICE)

    LOCATION_CHOICE = (
        ('hyderabad','Hyderabad'),
        ('bangalore','Bangalore'),
        ('chennai','Chennai'),
        ('pune','Pune')
        
    )
    location=MultiSelectFormField(max_length=100,choices=LOCATION_CHOICE)

    GENDER_CHOICE=(
            ('m','Male'),
            ('f','Female')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(),choices=GENDER_CHOICE
    ) 
    date=forms.DateField(
        widget=forms.SelectDateWidget()
        
    )

