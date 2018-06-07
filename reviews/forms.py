from django.forms import ModelForm, Textarea
from reviews.models import Review
from django import forms


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }

class FormName(forms.Form):
    fixedacid = forms.FloatField()
    volatileacid = forms.FloatField()
    criticacid = forms.FloatField()
    residualsugar = forms.FloatField()
    chloride = forms.FloatField()
    freesulpherdioxide = forms.FloatField()
    totalsulpherdioxide = forms.FloatField()
    density = forms.FloatField()
    ph = forms.FloatField()
    sulphate = forms.FloatField()
    alcohol = forms.FloatField()
