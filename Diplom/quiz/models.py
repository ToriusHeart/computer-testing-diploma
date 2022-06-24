from django.db import models

from django.conf import settings
#from django.contrib.auth.models import User
from django.dispatch import receiver

from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify

'''import os

def content_file_name(instance):
    return os.path.join('audio', "{}".format(instance.file.name))'''

# Create your models here.
class Test(models.Model):
    """
    Модель, представляющая тест (в случае данной работы - только 1 тест)
    """
    name = models.CharField(max_length=50, help_text="Введите название теста")
    desc = models.TextField(max_length=200, help_text="Описание теста")
    slug = models.SlugField(blank=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000, help_text="Введите описание задания")
    audio = models.FileField(blank=True,null=True,help_text="Добавляйте аудио-файлы при необходимости")
    order = models.IntegerField(default=0)
    
    QUESTION_TYPE = (
        ('l', 'Check your listening skills'),
        ('p', 'Check your pronunciation skills'),
        ('v', 'Determine if the consonants are voiced or voiceless')
    )

    quesType = models.CharField(max_length=1, choices=QUESTION_TYPE, blank=True, default='l', help_text='Тип вопроса')
    
    def __str__(self):
        if self.quesType=='l':
            return '%s, %d (Listening)' % (self.test.name, self.order)
        else:
            return '%s, %d (Pronunciation)' % (self.test.name, self.order)
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    label = models.CharField(max_length=150,help_text="Ответ")
    is_correct = models.BooleanField(default=False)
    audio = models.FileField(blank=True,null=True,help_text="Аудио-файлы при необходимости")
    
    def __str__(self):
        return 'Вопрос %d, \"%s\"' % (self.question.order, self.label)
    
'''class AnswerVV(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    VV_Type = (
        ('voiced', 'This consonant is voiced'),
        ('voiceless', 'This consonant is voiceless')
    )

    answType = models.CharField(max_length=9, choices=VV_Type, blank=True, default='voiced', help_text='Тип согласной')
'''
class AudioAnswer(models.Model):
    audiofile = models.FileField(blank=True,null=True,help_text="Аудио-файлы при необходимости")
    def __str__(self):
        return self.audiofile.name

class Student(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
        
class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    audio = models.ForeignKey(AudioAnswer, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        if self.answer == None:
            return 'Студент %s %s, группа %s, %s, %d, Нет ответа' % (self.student.user.last_name, 
                                                        self.student.user.first_name, 
                                                        self.student.user.group_number, 
                                                        self.question.test.name,
                                                        self.question.order)
        elif self.answer.is_correct == True:
            return 'Студент %s %s, группа %s, %s, %d, Ответ %s - правильный' % (self.student.user.last_name, 
                                                        self.student.user.first_name, 
                                                        self.student.user.group_number, 
                                                        self.question.test.name,
                                                        self.question.order,
                                                        self.answer.label)
                                                        
        else:
            return 'Студент %s %s, группа %s, %s, %d, Ответ %s - неправильный' % (self.student.user.last_name, 
                                                        self.student.user.first_name, 
                                                        self.student.user.group_number, 
                                                        self.question.test.name,
                                                        self.question.order,
                                                        self.answer.label)
        
@receiver(pre_save, sender=Test)
def slugify_name(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)