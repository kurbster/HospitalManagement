from django import forms
from django.contrib.auth.models import User
from . import models

#for admin signup
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

#for doctor related form
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','status','profile_pic']

class DiagnosisForm(forms.ModelForm):
    class Meta:
        model=models.Diagnosis
        fields=['first_name', 'last_name','mobile','feedback', 'symptoms', 'address', 'lab_work_required']

#for hospital staff related form
class HospitalStaffUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class HospitalStaffForm(forms.ModelForm):
    class Meta:
        model=models.HospitalStaff
        fields=['status']

class PatientForm(forms.ModelForm):
    #this is the extrafield for linking patient and their assigend doctor
    #this will show dropdown __str__ method doctor model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in Doctor model and return it
    assignedDoctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Patient
        fields=['address','mobile','status','symptoms','profile_pic', 'medicalHistory', 'patientInsuranceProvider','patientPolicyNumber']

#for student related form
class LabStaffUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class InsuranceForm(forms.ModelForm):
    class Meta:
        model=models.Insurance
        fields=['address','mobile','company','status','profile_pic']

class InsuranceUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

#for patient related form
class PatientUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class LabStaffForm(forms.ModelForm):
    class Meta:
        model=models.LabStaff
        fields=['address','mobile','department','status','profile_pic']


class LabTestRecordUserForm(forms.ModelForm):
    class Meta:
        model = models.Patient_LabTest_Records
        fields = ['patient','labtest','status']

class LabTestsUserForm(forms.ModelForm):
    class Meta:
        model = models.LabTests
        fields = '__all__'

class AppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patientId=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']

class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']

class PatientPaymentForm(forms.Form):
    paymentAmount = forms.IntegerField(min_value=0, label="Payment Amount")
    remainingAmount = forms.IntegerField(disabled=True, label="Remaining Amount", required=False)

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

# For submitting a OTP
class OneTimePasswordForm(forms.Form):
    code = forms.CharField(max_length=6, min_length=6, required=True)