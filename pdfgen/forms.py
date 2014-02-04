from django import forms
from parts.models import Part
from django_select2 import *

class PartChoice(AutoModelSelect2Field):
    queryset = Part.objects
    search_fields = ['part_number__istartswith',]
    
class MTRForm(forms.Form):
    CERT_TYPES = (
                    ('STUD', 'TSA Weld Stud'),
                    ('DBA', 'TSA DBA'),  
                ) 
    part_number = PartChoice()
    cert_type = forms.ChoiceField(choices=CERT_TYPES)
    heat_number = forms.CharField()
    aisi_grade = forms.CharField()
    size = forms.CharField()
    carbon = forms.CharField()
    manganese = forms.CharField()
    sulfur = forms.CharField()
    silicon = forms.CharField()
    phosphorus = forms.CharField()
    chromium = forms.CharField(required=False)
    aluminum = forms.CharField(required=False)
    nickel = forms.CharField(required=False)
    molybdenum = forms.CharField(required=False)
    other = forms.CharField(required=False)
    
    tensile_strength = forms.CharField(required=False)
    yield_strength = forms.CharField()
    reduction_of_area = forms.CharField()
    elongation = forms.CharField()
    