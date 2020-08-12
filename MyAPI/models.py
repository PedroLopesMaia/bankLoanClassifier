from django.db import models

# Create your models here.
class approvals(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    MARRIED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    GRADUATED_CHOICES = (
        ('Graduated', 'Graduated'),
        ('Not_Graduated', 'Not_Graduated')
    )

    SELFEMPLOYED_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    PROPERTY_CHOICES = (
        ('Rural', 'Rural'),
        ('Semiurban', 'Semiurban'),
        ('Urban', 'Urban')
    )

    Firstname=models.CharField(max_length=15)
    Lastname=models.CharField(max_length=15)
    Dependants=models.IntegerField(default=0)
    Applicantincome=models.IntegerField(default=0)
    Coapplicantincome=models.IntegerField(default=0)
    Loanamt=models.IntegerField(default=0)
    Loanterm=models.IntegerField(default=0)
    Credithistory=models.IntegerField(default=0)
    Gender=models.CharField(max_length=15, choices=GENDER_CHOICES)
    Married=models.CharField(max_length=15, choices=MARRIED_CHOICES)
    Graduatededucation=models.CharField(max_length=15, choices=GRADUATED_CHOICES)
    Selfemployed=models.CharField(max_length=15, choices=SELFEMPLOYED_CHOICES)
    Area=models.CharField(max_length=15, choices=PROPERTY_CHOICES)

    def __str__(self):
        return self.firstname, self.lastname