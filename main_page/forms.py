from django import forms


class DataForm(forms.Form):
    PPM = forms.CharField(label='PPM', max_length=100),
    OT = forms.CharField(label='OT', max_length=100),
    IT = forms.CharField(label='IT', max_length=100),
    IH = forms.CharField(label='IH', max_length=100),
    OH = forms.CharField(label='OH', max_length=100),
    AP = forms.CharField(label='AP', max_length=100),
    Time = forms.CharField(label='Time', max_length=100),
    Date = forms.CharField(label='DATE', max_length=100)
