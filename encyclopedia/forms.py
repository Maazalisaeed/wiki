from django import forms
# this will creat my coustom form for the edit and new pages with title being charater feild and content with a text are box
class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", max_length=200, widget=forms.TextInput(attrs={'class':"round"}),required=True)
    content = forms.CharField(label="Content in Markdown", widget=forms.Textarea, required=True)
