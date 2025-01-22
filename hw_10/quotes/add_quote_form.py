from django import forms

class AuthorQuoteForm(forms.Form):
    fullname = forms.CharField(label="Full Name", max_length=100)
    born_date = forms.CharField(label="Born Date", max_length=100)
    born_location = forms.CharField(label="Born Location", max_length=200)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    quote = forms.CharField(label="Quote", widget=forms.Textarea)
    tags = forms.CharField(label="Tags (comma-separated)", max_length=200)


    class Meta:
        fields = ['fullname', 'born_date', 'born_location', 'description', 'quote', 'tags']