from django import forms
from .models import Review
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label='Your name' ,max_length=100, error_messages={"required":"Please enter", 
#                                 "max_length":"max length is100"})
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=100)
#     rating=forms.IntegerField(label='Your Rating' ,min_value=1, max_value=5)
     
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = 'user_name'
        labels = {
            "user_name":"Your User Name",
            "review_text":"Your Feedback",
            "rating": "Your Rating"
        }
        error_messages ={
            "user_name":{
                "required":"Must not be empty",
                "max_length":"Please enter s hort"
            }
        }