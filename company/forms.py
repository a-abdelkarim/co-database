from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name', 
            'description', 
            'photo', 
            'activity', 
            'category',
            'address',
            'country',
            'state',
            'city',
            'street',
            'building_no',
            'phone',
            'website',
            'email',
            'latitude',
            'longitude'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'photo': forms.FileInput(attrs={'class': 'form-control', 'rows': 3}),
            'activity': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'building_no': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'latitude': forms.TextInput(attrs={'class': 'form-control'}),
            'longitude': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Company Name',
            'description': 'Description',
            'photo': 'Photo',
            'activity': 'Activity',
            'category': 'Category',
            'address': 'Address',
            'country': 'Country',
            'state': 'State/Province',
            'city': 'City',
            'street': 'Street',
            'building_no': 'Building No.',
            'phone': 'Phone',
            'website': 'Website',
            'email': 'Email',
            'latitude': 'Latitude',
            'longitude': 'Longitude',
        }