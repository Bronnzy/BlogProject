from django import forms


class EmailPostForm(forms.Form):
    name: forms.CharField = forms.CharField(max_length=30)
    email: forms.EmailField = forms.EmailField()
    to: forms.CharField = forms.CharField()
    comments: forms.CharField = forms.CharField(
        required = False,
        widget=forms.Textarea
        )
