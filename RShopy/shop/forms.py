from django import forms


class PrimeForm(forms.Form):
    number = forms.IntegerField(label='Enter a number')



