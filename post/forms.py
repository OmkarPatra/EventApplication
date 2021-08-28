from django import forms
from .models import EventList



class PostForm(forms.ModelForm):
    class Meta:
        model = EventList
        fields = ['title','host','image','event_date','event_time','location','price']

        widgets={
            'title' : forms.TextInput(attrs={'class' : 'form-control','placeholder':'Title'}),
            'host' : forms.Select(attrs={'class' : 'form-control','placeholder':'Host'}),
            'image' : forms.FileInput(attrs={'class' : 'form-control'}),
            'event_date' : forms.DateInput(attrs={'class' : 'form-control','type' : 'date'}),
            'event_time' : forms.TimeInput(attrs={'class' : 'form-control','type' : 'time'}),
            
            'location' : forms.TextInput(attrs={'class' : 'form-control'}),
            'price' : forms.TextInput(attrs={'class' : 'form-control'}),
            


        }