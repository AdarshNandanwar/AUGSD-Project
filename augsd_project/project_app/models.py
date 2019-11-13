# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Room(models.Model):
    roomNumber = models.CharField(max_length = 50, primary_key=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.roomNumber

class Course(models.Model):
    courseCode = models.CharField(max_length=10, primary_key=True)
    courseName = models.CharField(max_length=100)
    courseIC = models.ForeignKey(Instructor,related_name="InstructorIncharge",default=None)
    midsemDateTime = models.DateTimeField(null=False)
    compreDateTime = models.DateTimeField(null=False)

    def __str__(self):
        return self.courseCode

class Section(models.Model):
    course = models.ForeignKey(Course,related_name="section",default=None)
    sectionNumber = models.IntegerField()

    def __str__(self):
        return self.course.courseCode+','+str(self.sectionNumber)

class SubSection(models.Model):
    TYPE_CHOICES = (
        ('L', 'Lecture'),
        ('T', 'Tutorial'),
        ('P', 'Practical'),
        ('I', 'Independent'),
    )
    section = models.ForeignKey(Section,related_name="subSection",default=None)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    instructor1 = models.ForeignKey(Instructor, related_name='subSection1', default=None)   #backward relationship
    instructor2 = models.ForeignKey(Instructor, related_name='subSection2', default=None, null=True, blank=True)   #backward relationship
    days = models.CharField(max_length = 6, validators=[MinLengthValidator(6)])
    startTime = models.IntegerField()
    endTime = models.IntegerField()
    room = models.ForeignKey(Room, related_name='subSection', default=None)

    def __str__(self):
        return self.section.course.courseName+','+str(self.section.sectionNumber)+','+self.type