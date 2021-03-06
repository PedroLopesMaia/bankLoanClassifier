from django import forms

class ApprovalForm(forms.Form):
    firstname=forms.CharField(max_length=15)
    lastname=forms.CharField(max_length=15)
    dependants=forms.IntegerField()
    applicantincome=forms.IntegerField()
    coapplicantincome=forms.IntegerField()
    loanamt=forms.IntegerField()
    loanterm=forms.IntegerField()
    credithistory=forms.IntegerField()
    gender=forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    married=forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    graduatededucation=forms.ChoiceField(choices=[('Graduated', 'Graduated'), ('Not_Graduated', 'Not_Graduated')])
    selfemployed=forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])
    area=forms.ChoiceField(choices=[('Rural', 'Rural'), ('Semiurban', 'Semiurban'), ('Urban', 'Urban')])