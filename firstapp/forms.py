from django import forms
from models import Payment

class PaymentForm(forms.ModelForm):
   class Meta:
     model=Payment
     fields = ('name','amount','product')
  
  
      # name = forms.CharField(label=' Name', max_length=100)
      # amount =forms.IntegerField()
      # product = forms.CharField(max_length=300)

      # def __str__(self):
      #   return self.name