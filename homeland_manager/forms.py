from django import forms

class MonthlyBills(forms.Form):
    cleaner_tax = forms.IntegerField(label='Cleaner tax')
    stairs_electricity = forms.IntegerField(label='Stairs electricity')
    elevator_electricity = forms.IntegerField(label='Elevator electricit')
    other_common = forms.IntegerField(label='Other common payments')
    other_elevator = forms.IntegerField(label='Other elevator payments')
    common_comment = forms.CharField(label='Common comment', max_length=10)
    elevator_comment = forms.CharField(label='Elevator comment', max_length=10)