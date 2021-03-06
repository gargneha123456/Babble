# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from accounts.models import student, society
from django.db import models

# Create your models here.
class Announcement( models.Model ):
    AID = models.IntegerField(primary_key=True)
    CR_ID = models.ForeignKey(student, on_delete=models.CASCADE)
    CID = models.ForeignKey(society, on_delete= models.CASCADE)
    Subject = models.TextField()
    Timestamp = models.DateTimeField()
    Content = models.TextField()