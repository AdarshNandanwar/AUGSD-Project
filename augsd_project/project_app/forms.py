from django import forms  
from .models import Instructor, SubSection
  
class InstructorForm(forms.ModelForm):  
    class Meta:  
        model = Instructor  
        fields = "__all__"  

class SubSectionForm(forms.ModelForm):  
    class Meta:  
        model = SubSection  
        fields = "__all__"  