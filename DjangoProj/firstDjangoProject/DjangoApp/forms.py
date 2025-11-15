from django import forms
from .models import chaiVariety

# Example form for chaiVariety (if needed in future)
class ChaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=chaiVariety.objects.all(), label='Select Chai Variety')
    

