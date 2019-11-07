# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Room(models.Model):
    roomNumber = models.CharField(max_length = 50)
    capacity = models.IntegerField()
    def __str__(self):
        return self.roomNumber

class Course(models.Model):
    courseCode = models.CharField(max_length=10)
    courseName = models.CharField(max_length=100)
    midsemDateTime = models.DateTimeField(null=False)
    compreDateTime = models.DateTimeField(null=False)
    courseIC = models.ForeignKey(Instructor,related_name="InstructorIncharge",default=None)
    def __str__(self):
        return self.courseCode

class Section(models.Model):
    course = models.ForeignKey(Course,related_name="section",default=None)
    ltp = models.CharField(max_length = 3, default="000")        #just to store what types of subsections does this course have

class SubSection(models.Model):
    instructor1 = models.ForeignKey(Instructor, related_name='subSection1', default=None)   #backward relationship
    instructor2 = models.ForeignKey(Instructor, related_name='subSection2', default=None, blank=True)   #backward relationship
    days = models.CharField(max_length = 7)
    startTime = models.IntegerField()
    endTime = models.IntegerField()
    room = models.ForeignKey(Room, related_name='subSection', default=None)
    type = models.CharField(max_length = 1)
    section = models.ForeignKey(Section,related_name="subSection",default=None)