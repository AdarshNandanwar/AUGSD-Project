from django import forms  
from .models import Instructor, SubSection, Course, Section
  
class InstructorForm(forms.ModelForm):  
    class Meta:  
        model = Instructor  
        fields = "__all__"  

class SubSectionForm(forms.ModelForm):  
    class Meta:  
        model = SubSection  
        fields = "__all__"  

class CourseForm(forms.ModelForm):  
    class Meta:  
        model = Course  
        fields = "__all__"  

class SectionForm(forms.ModelForm):  
    class Meta:  
        model = Section  
        fields = "__all__"  