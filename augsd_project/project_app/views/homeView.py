from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect

from django.views import View
from project_app.forms import *
from project_app.models import *

class HomeView(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request, 'homePage.html')

class AddCourseForm(View):
    form_class = CourseForm
    initial = {'key': 'value'}
    template_name = 'addCourseForm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

class AddSectionForm(View):
    form_class = SectionForm
    initial = {'key': 'value'}
    template_name = 'addSectionForm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>

            course = form.cleaned_data.get('course')
            formSectionNumber = form.cleaned_data.get('sectionNumber')
            sectionList = course.section.all()
            isValid = True
            for s in sectionList:
                if(s.sectionNumber == formSectionNumber):
                    isValid = False
                    message = "Section number "+formSectionNumber+" already exists in this course"

            if(isValid):
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(message)
                # show some message when the form is not saved

        return render(request, self.template_name, {'form': form})

class AddSubSectionForm(View):
    form_class = SubSectionForm
    initial = {'key': 'value'}
    template_name = 'addSubSectionForm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>

            isValid = True
            formType = form.cleaned_data.get('type')
            formSection = form.cleaned_data.get('section')
            formRoom = form.cleaned_data.get('room')
            formStartTime = form.cleaned_data.get('startTime')
            formEndTime = form.cleaned_data.get('endTime')
            formDays = form.cleaned_data.get('days')
            formInstructor1 = form.cleaned_data.get('instructor1')
            formInstructor2 = form.cleaned_data.get('instructor2')

            if(formStartTime>=formEndTime):
                isValid = False
                message = "Start time must be less than end time!"
            if(formDays=="0000000"):
                isValid = False
                message = "Please select atleast 1 day"
            if(formInstructor1==formInstructor2):
                isValid = False
                message = "Two instructors can't be same" 
            # checking if subSection already exists
            repeatingSubSectionList = SubSection.objects.filter(section=formSection, type=formType)
            print(repeatingSubSectionList)
            if repeatingSubSectionList.exists():
                isValid = False
                message = "This SubSection already exists."

            if not isValid:
                print(message)
                return render(request, self.template_name, {'form': form})
                # show some message when the form is not saved 

            # checking clashes with classroom
            subSectionList = formRoom.subSection.all()
            for ss in subSectionList:
                for dayNumber in range(7):
                    if (ss.days[dayNumber]=='1' and formDays[dayNumber]=='1'):
                        if not(int(formEndTime)<=int(ss.startTime) or int(ss.endTime)<=int(formStartTime)):
                            isValid = False
                            message = "Class is already occupied by "+str(ss)+"!"

            if not isValid:
                print(message)
                return render(request, self.template_name, {'form': form})
                # show some message when the form is not saved 

            # checking clashes with Instructors
            subSectionList1 = formInstructor1.subSection1.all() | formInstructor1.subSection2.all()
            subSectionList2 = formInstructor2.subSection1.all() | formInstructor2.subSection2.all()
            print(subSectionList1)
            print(subSectionList2)
            for ss in subSectionList1:
                for dayNumber in range(7):
                    if (ss.days[dayNumber]=='1' and formDays[dayNumber]=='1'):
                        if not(int(formEndTime)<=int(ss.startTime) or int(ss.endTime)<=int(formStartTime)):
                            isValid = False
                            message = formInstructor1.name+" is not free at this time."
            for ss in subSectionList2:
                for dayNumber in range(7):
                    if (ss.days[dayNumber]=='1' and formDays[dayNumber]=='1'):
                        if not(int(formEndTime)<=int(ss.startTime) or int(ss.endTime)<=int(formStartTime)):
                            isValid = False
                            message = formInstructor2.name+" is not free at this time."

            if(isValid):
                form.save()
                return HttpResponseRedirect('/')
            else:
                print(message)
                return render(request, self.template_name, {'form': form})
                # show some message when the form is not saved 

        return render(request, self.template_name, {'form': form})



class DeleteCourseForm(View):
    form_class = DeleteCourseForm
    initial = {'key': 'value'}
    template_name = 'deleteCourseForm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            # add delte logic here

            # c = Course.objects.filter(courseCode=form.cleaned_data['courseCode'])
            # print(type(c))
            # for course in c:
            #     print(type(course))
            #     print(type(course.section))

            c = Course.objects.get(courseCode=form.cleaned_data['courseCode'])
            print(c)
            print(c.section)
                
            s.delete()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

class DeleteSectionForm(View):
    form_class = DeleteSectionForm
    initial = {'key': 'value'}
    template_name = 'deleteSectionForm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            # add delte logic here
            s = Section.objects.filter(course=form.instance.course, sectionNumber=form.instance.sectionNumber)
            s.delete()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

class DeleteSubSectionForm(View):
    form_class = DeleteSubSectionForm
    initial = {'key': 'value'}
    template_name = 'deleteSubSectionForm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            s = SubSection.objects.filter(section=form.instance.section, type=form.instance.type)
            s.delete()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})



class ModifyCourseForm(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request, 'modifyCourseForm.html')

class ViewTimetableForm(View):
    form_class = ViewInstructorForm
    initial = {'key': 'value'}
    template_name = 'viewTimetableForm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'displayTable': False})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            # form.save()
            instr = form.cleaned_data.get('instructorName')
            sectionList = instr.subSection1.all() | instr.subSection2.all()
            return render(request, self.template_name, {'form': form, 'sectionList': sectionList, 'displayTable': sectionList.exists()})
            # return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})