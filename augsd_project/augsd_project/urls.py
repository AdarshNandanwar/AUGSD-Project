"""augsd_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
# from project_app import views
import project_app.views as VIEWS


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add-course/', VIEWS.AddCourseForm.as_view()),
    url(r'^add-section/', VIEWS.AddSectionForm.as_view()),
    url(r'^add-subsection/', VIEWS.AddSubSectionForm.as_view()),
    url(r'^modify-course/', VIEWS.ModifyCourseForm.as_view()),
    url(r'^modify-section/', VIEWS.ModifySectionForm.as_view()),
    url(r'^modify-subsection/', VIEWS.ModifySubSectionForm.as_view()),
    url(r'^delete-course/', VIEWS.DeleteCourseForm.as_view()),
    url(r'^delete-section/', VIEWS.DeleteSectionForm.as_view()),
    url(r'^delete-subsection/', VIEWS.DeleteSubSectionForm.as_view()),
    url(r'^view-instructor-timetable/', VIEWS.ViewInstructorTimetableForm.as_view()),
    url(r'^view-room-timetable/', VIEWS.ViewRoomTimetableForm.as_view()),
    url(r'^download-timetable/', VIEWS.DownloadTimeTable.as_view()),
    url(r'^$', VIEWS.HomeView.as_view(), name='home'),
]
