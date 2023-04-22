from django import forms

class ProfesorForm(forms.Form):
    
    apellido= forms.CharField(max_length=50)
    nombre= forms.CharField(max_length=50)
    profesion= forms.CharField(max_length=50)
    email= forms.EmailField()
    