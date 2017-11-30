from django import forms


class DataForm(forms.Form):
    url = forms.CharField(label='URL', max_length=100)
    port = forms.CharField(label='PORT', max_length=40)
    body = forms.CharField(label='Request Body', max_length=1000)
    # date = forms.DateField(label='Date')
