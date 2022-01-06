from django import forms
from .models import Marker
from datetime import datetime


class MarkerForm(forms.Form):
    name = forms.CharField(max_length=100,widget=forms.TextInput)
    latitude = forms.FloatField(required=False, max_value=90, min_value=-90)
    longitude = forms.FloatField(required=False, max_value=180, min_value=-180)
    expire_date =  forms.DateField(widget=forms.SelectDateWidget)
    id = forms.CharField(widget=forms.HiddenInput(), required=False)

    def clean_expire_date(self):
        expire_date = self.cleaned_data.get('expire_date')
        print(str(expire_date)+" data")
        today = datetime.today().date()
        if expire_date > today:
            return expire_date
        else:
            raise forms.ValidationError('A data de experição precisa ser maior que hoje')

    def update(self):
        data = self.cleaned_data
        id = data['id']
        if id:
            myRegister = Marker.objects.filter(id=id)
            if (myRegister):
                myRegister = myRegister[0]
                myRegister.name = data['name']
                myRegister.latitude = data['latitude']
                myRegister.longitude = data['longitude']
                myRegister.expire_date = data['expire_date']
                myRegister.save()
                return myRegister
        return None
    def save(self):
        data = self.cleaned_data
        myRegister = Marker.objects.create(
            name=data['name'],
            latitude=data['latitude'],
            longitude=data['longitude'],
            expire_date = data['expire_date'],
        )
        return myRegister
