from django import forms


class BadAppForm(forms.Form):
    left_name1 = forms.CharField(
        label='名前',
        max_length=10,
        required=True,
        widget=forms.TextInput()
    )

    left_name2 = forms.CharField(
        label='名前',
        max_length=10,
        required=True,
        widget=forms.TextInput()
    )

    right_name1 = forms.CharField(
        label='名前',
        max_length=10,
        required=True,
        widget=forms.TextInput()
    )

    right_name2 = forms.CharField(
        label='名前',
        max_length=10,
        required=True,
        widget=forms.TextInput()
    )
