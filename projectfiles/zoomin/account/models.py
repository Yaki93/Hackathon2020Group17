from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    First_Name = models.CharField('שם פרטי', max_length=30, null=True, blank=True)
    Last_Name = models.CharField('שם משפחה', max_length=30, null=True, blank=True)
    Code = models.CharField('קוד הרשאה', max_length=30, null=True, blank=True)
    ID_Number = models.CharField('תעודת זהות', max_length=30, null=True, blank=True)

    class Meta:
        verbose_name_plural = "userprofile"

    def __str__(self):
        return str(self.user)


class board_school(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField('נושא',max_length=100, blank=False, null=False)
    description = models.TextField('תיאור', max_length=300, blank=True , null=True)
    publication_date = models.DateField('תאריך',default=date.today())

    class Meta:
        verbose_name = 'Board_school'
        verbose_name_plural = 'Board_school'
        ordering = ['publication_date']


    def __str__(self):
        return self.topic


class board_class(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.CharField('נושא',max_length=100, blank=False, null=False)
    description = models.TextField('תיאור', max_length=300, blank=True , null=True)
    publication_date = models.DateField('תאריך',default=date.today())
    class Meta:
        verbose_name = 'Board_class'
        verbose_name_plural = 'Board_class'
        ordering = ['publication_date']


    def __str__(self):
        return self.topic


class schedule_mod(models.Model):
    id = models.AutoField(primary_key=True)
    friday = models.CharField('יום שישי',max_length=100, blank=False, null=False)
    friday_link = models.CharField('קישור-יום שישי',max_length=100, blank=False, null=False)
    thursday = models.CharField('יום חמישי',max_length=100, blank=False, null=False)
    thursday_link = models.CharField('קישור-יום חמישי',max_length=100, blank=False, null=False)
    wednesday = models.CharField('יום רביעי',max_length=100, blank=False, null=False)
    wednesday_link = models.CharField('קישור-יום רביעי',max_length=100, blank=False, null=False)
    tuesday = models.CharField('יום שלישי',max_length=100, blank=False, null=False)
    tuesday_link = models.CharField('קישור-יום שלישי',max_length=100, blank=False, null=False)
    monday = models.CharField('יום שני',max_length=100, blank=False, null=False)
    monday_link = models.CharField('קישור-יום שני',max_length=100, blank=False, null=False)
    sunday = models.CharField('יום ראשון',max_length=100, blank=False, null=False)
    sunday_link = models.CharField('קישור-יום ראשון',max_length=100, blank=False, null=False)
    time = models.CharField('שעה',max_length=100, blank=False, null=False)
    topics = [friday, friday_link, thursday, thursday_link, wednesday, wednesday_link,
              tuesday, tuesday_link, monday, monday_link, sunday, sunday_link, time]

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedule'

    def __str__(self):
        return self.topics

class Test_Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    profession = models.CharField('מקצוע',max_length=100, blank=False, null=False)
    date = models.DateField('תאאריך',default=date.today(), blank=True , null=True)
    start_time = models.TimeField('שעת התחלה',auto_now=False, auto_now_add=False, null=True)
    end_time = models.TimeField('שעת סיום',auto_now=False, auto_now_add=False, null=True)
    class Meta:
        verbose_name = 'Test_Schedule'
        verbose_name_plural = 'Test_Schedule'
        ordering = ['date']


    def __str__(self):
        return self.profession