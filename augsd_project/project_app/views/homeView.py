import csv
from django.http import HttpResponse

from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.forms.models import model_to_dict

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
            messages.success(request, "Course added successfully.", extra_tags='alert-success')
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
                    message = "Section number "+str(formSectionNumber)+" already exists in this course"
                    
            if(isValid):
                form.save()
                messages.success(request, "Section added successfully.", extra_tags='alert-success')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, message, extra_tags='alert-danger')

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
                message = "Start time must be less than end time."
            if(formDays=="0000000"):
                isValid = False
                message = "Please select atleast 1 day"
            if(formInstructor1==formInstructor2):
                isValid = False
                message = "Two instructors can't be same" 
            # checking if subSection already exists
            repeatingSubSectionList = SubSection.objects.filter(section=formSection, type=formType)
            if repeatingSubSectionList.exists():
                isValid = False
                message = "This SubSection already exists."

            if not isValid:
                messages.error(request, message, extra_tags='alert-danger')
                return render(request, self.template_name, {'form': form})

            # checking clashes with classroom
            subSectionList = formRoom.subSection.all()
            for ss in subSectionList:
                for dayNumber in range(6):
                    if (ss.days[dayNumber]=='1' and formDays[dayNumber]=='1'):
                        if not(int(formEndTime)<=int(ss.startTime) or int(ss.endTime)<=int(formStartTime)):
                            isValid = False
                            message = "Class is already occupied by "+str(ss)+"."

            if not isValid:
                messages.error(request, message, extra_tags='alert-danger')
                return render(request, self.template_name, {'form': form})

            # checking clashes with Instructors
            subSectionList1 = formInstructor1.subSection1.all() | formInstructor1.subSection2.all()
            for ss in subSectionList1:
                for dayNumber in range(6):
                    if (ss.days[dayNumber]=='1' and formDays[dayNumber]=='1'):
                        if not(int(formEndTime)<=int(ss.startTime) or int(ss.endTime)<=int(formStartTime)):
                            isValid = False
                            message = formInstructor1.name+" is not free at this time."
            if formInstructor2 is not None:
                subSectionList2 = formInstructor2.subSection1.all() | formInstructor2.subSection2.all()
                for ss in subSectionList2:
                    for dayNumber in range(6):
                        if (ss.days[dayNumber]=='1' and formDays[dayNumber]=='1'):
                            if not(int(formEndTime)<=int(ss.startTime) or int(ss.endTime)<=int(formStartTime)):
                                isValid = False
                                message = formInstructor2.name+" is not free at this time."

            if(isValid):
                form.save()
                messages.success(request, "Sub section added successfully.", extra_tags='alert-success')
                return HttpResponseRedirect('/')
            else:
                messages.error(request, message, extra_tags='alert-danger')
                return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})

class ModifyCourseForm(generic.TemplateView):
    form_class = EditCourseForm
    modify_form_class = ModifyCourseForm
    initial = {'key': 'value'}
    template_name = 'modifyCourseForm.html'
    modify_template_name = 'modifySelectedCourseForm.html'

    def get(self, request, *args, **kwargs):
        paramsCourseCode = request.GET.get('courseCode', None)
        if paramsCourseCode is None:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            courseList = Course.objects.filter(courseCode=paramsCourseCode) 
            if courseList:
                form = self.modify_form_class(instance=courseList.first())
                return render(request, self.modify_template_name, {'form': form, 'courseCode': paramsCourseCode})
            else:
                form = self.form_class(initial=self.initial)
                messages.error(request, "Course not found.", extra_tags='alert-danger')
                return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.modify_form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            currentCourseCode = request.POST.get('courseCode', None)
            Course.objects.filter(courseCode=currentCourseCode).update(courseName=form.cleaned_data['courseName'], courseIC=form.cleaned_data['courseIC'], midsemDateTime=form.cleaned_data['midsemDateTime'], compreDateTime=form.cleaned_data['compreDateTime'])
            messages.success(request, "Course modified successfully.", extra_tags='alert-success')
            return HttpResponseRedirect('/')

        return render(request, self.modify_template_name, {'form': form})

class ModifySectionForm(generic.TemplateView):
    form_class = EditSectionForm
    modify_form_class = ModifySectionForm
    initial = {'key': 'value'}
    template_name = 'modifySectionForm.html'
    modify_template_name = 'modifySelectedSectionForm.html'

    def get(self, request, *args, **kwargs):
        paramsCourse = request.GET.get('course', None)
        paramsSectionNumber = request.GET.get('sectionNumber', None)
        if paramsCourse is None:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            courseList = Course.objects.filter(courseCode=paramsCourse) 
            if courseList:
                sectionList = Section.objects.filter(course=courseList.first(), sectionNumber=paramsSectionNumber) 
                if sectionList:
                    form = self.modify_form_class(instance=sectionList.first())
                    return render(request, self.modify_template_name, {'form': form, 'course': paramsCourse, 'currentSectionNumber': paramsSectionNumber})
                else:
                    form = self.form_class(initial=self.initial)
                    messages.error(request, "Section not found.", extra_tags='alert-danger')
                    return render(request, self.template_name, {'form': form})
            else:
                form = self.form_class(initial=self.initial)
                messages.error(request, "Course not found.", extra_tags='alert-danger')
                return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.modify_form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            currentCourse = request.POST.get('course', None)
            currentSectionNumber = request.POST.get('currentSectionNumber', None)
            currentCourseList = Course.objects.filter(courseCode=currentCourse)
            # checking if sectionNumber is already in use
            sectionList = currentCourseList.first().section.all()
            for section in sectionList:
                if(section.sectionNumber == int(form.cleaned_data['sectionNumber'])):
                    message = "Section number "+str(form.cleaned_data['sectionNumber'])+" already exists in this course"
                    messages.error(request, message, extra_tags='alert-danger')
                    form = self.form_class(initial=self.initial)
                    return render(request, self.template_name, {'form': form})
            Section.objects.filter(course=currentCourseList.first(), sectionNumber=currentSectionNumber).update(sectionNumber=form.cleaned_data['sectionNumber'])
            messages.success(request, "Section modified successfully.", extra_tags='alert-success')
            return HttpResponseRedirect('/')

        return render(request, self.modify_template_name, {'form': form})

class ModifySubSectionForm(generic.TemplateView):
    form_class = EditSubSectionForm
    modify_form_class = ModifySubSectionForm
    initial = {'key': 'value'}
    template_name = 'modifySubSectionForm.html'
    modify_template_name = 'modifySelectedSubSectionForm.html'

    def get(self, request, *args, **kwargs):
        paramsSection = request.GET.get('section', None)
        paramsType = request.GET.get('type', None)
        print(paramsSection)
        if paramsSection is None:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})
        else:
            courseList = Course.objects.filter(courseCode=paramsCourse) 
            if courseList:
                SubSectionList = SubSection.objects.filter(course=courseList.first(), sectionNumber=paramsSectionNumber) 
                if SubSectionList:
                    form = self.modify_form_class(instance=sectionList.first())
                    return render(request, self.modify_template_name, {'form': form, 'course': paramsCourse, 'currentSectionNumber': paramsSectionNumber})
                else:
                    form = self.form_class(initial=self.initial)
                    messages.error(request, "Section not found.", extra_tags='alert-danger')
                    return render(request, self.template_name, {'form': form})
            else:
                form = self.form_class(initial=self.initial)
                messages.error(request, "Course not found.", extra_tags='alert-danger')
                return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.modify_form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            currentCourse = request.POST.get('course', None)
            currentSectionNumber = request.POST.get('currentSectionNumber', None)
            currentCourseList = Course.objects.filter(courseCode=currentCourse)
            Section.objects.filter(course=currentCourseList.first(), sectionNumber=currentSectionNumber).update(sectionNumber=form.cleaned_data['sectionNumber'])
            messages.success(request, "Section modified successfully.", extra_tags='alert-success')
            return HttpResponseRedirect('/')

        return render(request, self.modify_template_name, {'form': form})

class DeleteCourseForm(View):
    form_class = EditCourseForm
    initial = {'key': 'value'}
    template_name = 'deleteCourseForm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            courseList = Course.objects.filter(courseCode=form.cleaned_data['courseCode'])
            if courseList:
                for course in courseList:
                    course.delete()
                messages.success(request, "Course deleted successfully.", extra_tags='alert-success')
                return HttpResponseRedirect('/')
            else:
                message = "No such course exists"
                messages.error(request, message, extra_tags='alert-danger')
        return render(request, self.template_name, {'form': form})

class DeleteSectionForm(View):
    form_class = EditSectionForm
    initial = {'key': 'value'}
    template_name = 'deleteSectionForm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            sectionList = Section.objects.filter(course=form.instance.course, sectionNumber=form.instance.sectionNumber)
            if sectionList:
                for section in sectionList:
                    section.delete()
                messages.success(request, "Section deleted successfully.", extra_tags='alert-success')
                return HttpResponseRedirect('/')
            else:
                message = "No such section exists."
                messages.error(request, message, extra_tags='alert-danger')
        return render(request, self.template_name, {'form': form})

class DeleteSubSectionForm(View):
    form_class = EditSubSectionForm
    initial = {'key': 'value'}
    template_name = 'deleteSubSectionForm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            subSectionList = SubSection.objects.filter(section=form.instance.section, type=form.instance.type)
            if subSectionList:
                for subSection in subSectionList:
                    subSection.delete()
                messages.success(request, "Sub section deleted successfully.", extra_tags='alert-success')
                return HttpResponseRedirect('/')
            else:
                message = "No such sub section exists."
                messages.error(request, message, extra_tags='alert-danger')
        return render(request, self.template_name, {'form': form})

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
            instr = form.cleaned_data.get('instructorName')
            subSectionList = instr.subSection1.all() | instr.subSection2.all()
            return render(request, self.template_name, {'form': form, 'subSectionList': subSectionList, 'displayTable': subSectionList.exists()})
        return render(request, self.template_name, {'form': form})

class DownloadTimeTable(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="TimeTable.csv"'
        courseList = Course.objects.filter()
        writer = csv.writer(response)
        writer.writerow(['COURSENO', 'COURSETITLE', 'SEC', 'STAT', 'INSTRUCTOR IN CHARGE/Instructor', 'DAYS/ H', 'ROOM', 'COMPRE DATE'])
        for course in courseList:
            sectionList = course.section.all()
            for section in sectionList:
                subSectionList = section.subSection.all()
                for subSection in subSectionList:
                    formatedDaysTime = ""
                    for i in range(6):
                        if(subSection.days[i] == '0'):
                            continue
                        if(i==0):
                            formatedDaysTime += "M "
                        if(i==1):
                            formatedDaysTime += "T "
                        if(i==2):
                            formatedDaysTime += "W "
                        if(i==3):
                            formatedDaysTime += "TH "
                        if(i==4):
                            formatedDaysTime += "F "
                        if(i==5):
                            formatedDaysTime += "S "
                    for i in range(subSection.startTime, subSection.endTime):
                        formatedDaysTime += str(i-7) + " "
                    if(subSection.instructor1==course.courseIC):
                        formatedInstructor = subSection.instructor1.name.upper()
                    else:
                        formatedInstructor = subSection.instructor1.name
                    if subSection.instructor2 is not None:
                        if(subSection.instructor2==course.courseIC):
                            formatedInstructor += ", "+subSection.instructor2.name.upper() 
                        else:
                            formatedInstructor += ", "+subSection.instructor2.name
                    writer.writerow([course.courseCode,course.courseName,section.sectionNumber,subSection.type,formatedInstructor, formatedDaysTime, subSection.room, course.compreDateTime.strftime("%d/%m/%y %H")])
        return response