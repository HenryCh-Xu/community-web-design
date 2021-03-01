from django import forms
from .models import lost_find_topic
from .models import lost_find_entry
from .models import electronics_topic
from .models import electronics_entry
from .models import necessary_topic
from .models import necessary_entry

#失物招领
class LFT_Form(forms.ModelForm):
    class Meta:
        model = lost_find_topic
        fields = ['text']
        labels = {'text': ''}

class LFT_EntryForm(forms.ModelForm):
    class Meta:
        model = lost_find_entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

#电子产品
class ET_Form(forms.ModelForm):
    class Meta:
        model = electronics_topic
        fields = ['text']
        labels = {'text': ''}

class ET_EntryForm(forms.ModelForm):
    class Meta:
        model = electronics_entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

#日常用品
class NT_Form(forms.ModelForm):
    class Meta:
        model = necessary_topic
        fields = ['text']
        labels = {'text': ''}

class NT_EntryForm(forms.ModelForm):
    class Meta:
        model = necessary_entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

