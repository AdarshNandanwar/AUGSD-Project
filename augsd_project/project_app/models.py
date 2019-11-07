# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Instructor(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class SubSection(models.Model):
    instructor1 = models.ForeignKey(Instructor, related_name='subSection1', default=None)   #backward relationship
    instructor2 = models.ForeignKey(Instructor, related_name='subSection2', default=None, blank=True)   #backward relationship
    days = models.CharField(max_length = 7)
    startTime = models.IntegerField()
    endTime = models.IntegerField()
    # room = models.ForeignKey(Room, related_name='room', default=None)
    courseCode = models.CharField(max_length = 10)