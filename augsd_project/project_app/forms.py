from django import forms  
from .models import Instructor, SubSection, Course, Section
  
class ViewInstructorForm(forms.ModelForm):
    instructorName = forms.ModelChoiceField(queryset=Instructor.objects.all(), required=True, label="Instructor Name")   #backward relationship
    class Meta:  
        model = Instructor  
        fields = ['instructorName']

class CourseForm(forms.ModelForm):  
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
        fields = ['course','sectionNumber']
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
            "startTime": "Start Time",
            "endTime": "End Time",
        }

# class DeleteCourseForm(forms.ModelForm):  
#     class Meta:  
#         model = Course  
#         fields = ['courseCode']
#         labels = {
#             "courseCode": "Course Code",
#         }

class DeleteCourseForm(forms.Form):  
    courseCode = forms.CharField(max_length=10)


class DeleteSectionForm(forms.ModelForm):  
    class Meta:  
        model = Section  
        fields = ['course','sectionNumber']
        labels = {
            "sectionNumber": "Section Number",
        }

class DeleteSubSectionForm(forms.ModelForm):  
    class Meta:  
        model = SubSection  
        fields = ['section', 'type']