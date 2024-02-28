from django import forms

class NewPageForm(forms.Form):
    title = forms.CharField(label="Title",  max_length=200, required=True)
    content = forms.CharField(label="Content", widget=forms.Textarea, required=True)