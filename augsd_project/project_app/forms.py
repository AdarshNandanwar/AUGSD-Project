from django import forms  
from django.forms import DateTimeField
from .models import Instructor, SubSection, Course, Section
  
class ViewInstructorForm(forms.ModelForm):
    instructorName = forms.ModelChoiceField(queryset=Instructor.objects.all(), required=True, label="Instructor Name")   #backward relationship
    class Meta:  
        model = Instructor  
        fields = ['instructorName']

class CourseForm(forms.ModelForm):
    midsemDateTime = DateTimeField(input_formats=["%d/%m/%y %H"], label="Midsem Date and Time (dd/mm/yy h)")
    compreDateTime = DateTimeField(input_formats=["%d/%m/%y %H"], label="Compre Date and Time (dd/mm/yy h)")
    class Meta:  
        model = Course  
        fields = "__all__"  
        labels = {
            "courseCode": "Course Code",
            "courseName": "Course Name",
            "midsemDateTime": "Midsem Date and Time",
            "compreDateTime": "Compre Date and Time",
            "courseIC": "Course IC",
        }

class SectionForm(forms.ModelForm):  
    class Meta:  
        model = Section  
        fields = "__all__"  
        labels = {
            "sectionNumber": "Section Number",
        }

class SubSectionForm(forms.ModelForm):  
    class Meta:  
        model = SubSection  
        fields = "__all__"  
        labels = {
            "instructor1": "Instructor 1",
            "instructor2": "Instructor 2",
            "days": "Days(6 length bitstring M,W,F = 101010)",
            "startTime": "Start Time Hour(24 hour format)",
            "endTime": "End Time Hour(24 hour format)",
        }

class ModifyCourseForm(forms.ModelForm):
    midsemDateTime = DateTimeField(input_formats=["%d/%m/%y %H"], label="Midsem Date and Time (dd/mm/yy h)")
    compreDateTime = DateTimeField(input_formats=["%d/%m/%y %H"], label="Compre Date and Time (dd/mm/yy h)")
    class Meta:  
        model = Course  
        fields = ['courseName', 'courseIC','midsemDateTime','compreDateTime']
        labels = {
            "courseCode": "Course Code",
            "courseName": "Course Name",
            "midsemDateTime": "Midsem Date and Time",
            "compreDateTime": "Compre Date and Time",
            "courseIC": "Course IC",
        }

class ModifySectionForm(forms.ModelForm):  
    class Meta:  
        model = Section  
        fields = ['sectionNumber']
        labels = {
            "sectionNumber": "Section Number",
        }

class ModifySubSectionForm(forms.ModelForm):  
    class Meta:  
        model = SubSection  
        fields = "__all__"  
        labels = {
            "instructor1": "Instructor 1",
            "instructor2": "Instructor 2",
            "days": "Days(6 length bitstring M,W,F = 101010)",
            "startTime": "Start Time Hour(24 hour format)",
            "endTime": "End Time Hour(24 hour format)",
        }

class EditCourseForm(forms.Form):  
    courseCode = forms.CharField(max_length=10, label="Course Code")


class EditSectionForm(forms.ModelForm):  
    class Meta:  
        model = Section  
        fields = ['course','sectionNumber']
        labels = {
            "sectionNumber": "Section Number",
        }

class EditSubSectionForm(forms.ModelForm):  
    class Meta:  
        model = SubSection  
        fields = ['section', 'type']