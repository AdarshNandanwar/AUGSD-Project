from django import forms  
from django.forms import DateTimeField
from .models import Instructor, SubSection, Course, Section, Room
  
class ViewInstructorForm(forms.ModelForm):
    instructorName = forms.ModelChoiceField(queryset=Instructor.objects.all(), required=True, label="Instructor Name")   #backward relationship
    class Meta:  
        model = Instructor  
        fields = ['instructorName']

class ViewRoomForm(forms.ModelForm):
    room = forms.ModelChoiceField(queryset=Room.objects.all(), required=True, label="Room")   #backward relationship
    class Meta:  
        model = Room  
        fields = ['room']

class CourseForm(forms.ModelForm):
    courseCode = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder': 'e.g. CS F213'}))
    courseName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'e.g. OBJECT ORIENTED PROGRAMMING'}))
    midsemDateTime = DateTimeField(input_formats=["%d/%m/%y %H"], label="Midsem Date and Time (dd/mm/yy h)", widget=forms.TextInput(attrs={'placeholder': 'e.g. 4/10/19 9'}))
    compreDateTime = DateTimeField(input_formats=["%d/%m/%y %H"], label="Compre Date and Time (dd/mm/yy h)", widget=forms.TextInput(attrs={'placeholder': 'e.g. 9/12/19 14'}))
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
    sectionNumber = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'e.g. 1'}))
    class Meta:  
        model = Section  
        fields = "__all__"  
        labels = {
            "sectionNumber": "Section Number",
        }

class SubSectionForm(forms.ModelForm):  
    days = forms.CharField(max_length = 6, label="Days (6 length bitstring M,W,F = 101010)", widget=forms.TextInput(attrs={'placeholder': 'e.g. 101010'}))
    startTime = forms.IntegerField( label="Start Time Hour (24 hour format)", widget=forms.NumberInput(attrs={'placeholder': 'e.g. 14'}))
    endTime = forms.IntegerField( label="End Time Hour (24 hour format)", widget=forms.NumberInput(attrs={'placeholder': 'e.g. 15'}))
    class Meta:  
        model = SubSection  
        fields = "__all__"
        labels = {
            "instructor1": "Instructor 1",
            "instructor2": "Instructor 2"
        }

class ModifyCourseForm(forms.ModelForm):
    midsemDateTime = DateTimeField(widget=forms.widgets.DateTimeInput(format="%d/%m/%y %H"), input_formats=["%d/%m/%y %H"], label="Midsem Date and Time (dd/mm/yy h)")
    compreDateTime = DateTimeField(widget=forms.widgets.DateTimeInput(format="%d/%m/%y %H"), input_formats=["%d/%m/%y %H"], label="Compre Date and Time (dd/mm/yy h)")
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
        fields = ['type','instructor1','instructor2','days','startTime','endTime','room'] 
        labels = {
            "instructor1": "Instructor 1",
            "instructor2": "Instructor 2",
            "days": "Days (6 length bitstring M,W,F = 101010)",
            "startTime": "Start Time Hour (24 hour format)",
            "endTime": "End Time Hour (24 hour format)",
        }

class EditCourseForm(forms.Form):  
    courseCode = forms.CharField(max_length=10, label="Course Code", widget=forms.TextInput(attrs={'placeholder': 'e.g. CS F213'}))


class EditSectionForm(forms.ModelForm):  
    sectionNumber = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'e.g. 1'}))
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