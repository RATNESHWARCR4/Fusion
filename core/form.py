from core.models import Profile
from django.forms import ModelForm
from django.forms import widgets
from core.models import Music
from django import forms

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        exclude=['uuid']



class AddMusicForm(forms.ModelForm):
    album=forms.CharField(max_length=500,required=False)
    
    class Meta:
        model=Music
        fields=[
            'title',
            'artiste',
           
            'audio_file',
            'cover_image',
        ]
