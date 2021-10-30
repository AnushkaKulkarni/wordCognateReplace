from django import forms

class OriginalTextForm(forms.Form):
    output = forms.CharField(label='Original Text', max_length=2000)
