from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect

from django.views import View
from project_app.forms import InstructorForm, SubSectionForm

class HomeView(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request, 'homePage.html')

class AddCourseForm(View):
    form_class = SubSectionForm
    initial = {'key': 'value'}
    template_name = 'addCourseForm.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/')

        return render(request, self.template_name, {'form': form})

class ModifyCourseForm(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request, 'modifyCourseForm.html')

class DeleteCourseForm(generic.TemplateView):
	def get(self, request, *args, **kwargs):
		return render(request, 'deleteCourseForm.html')

