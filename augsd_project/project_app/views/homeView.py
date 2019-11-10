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
            form.save()
            return HttpResponseRedirect('/')

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
            form.save()
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})


# delete classes

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
                
            # s.delete()
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
        print(form)
        return render(request, self.template_name, {'form': form, 'displayTable': False})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            # form.save()
            instr = form.cleaned_data.get('instructorName')
            sectionList = instr.subSection1.all()
            return render(request, self.template_name, {'form': form, 'sectionList': sectionList, 'displayTable': sectionList.exists()})
            # return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})