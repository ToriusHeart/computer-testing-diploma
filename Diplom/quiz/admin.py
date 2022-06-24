from django.contrib import admin

import nested_admin
# Register your models here.

from .models import Test, Question, Answer, Student, StudentAnswer, AudioAnswer#, AnswerVV

#class AnswerVVInline(nested_admin.NestedTabularInline):
#    model = AnswerVV
 #   extra = 0
    
class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
#    inlines = [AnswerVVInline,]
    extra = 0
    
class AnswerAdmin(nested_admin.NestedModelAdmin):
#    inlines = [AnswerVVInline,]
    pass
    
class QuestionInline(nested_admin.NestedTabularInline):
	model = Question
	inlines = [AnswerInline,]
	extra = 0

class QuestionAdmin(nested_admin.NestedModelAdmin):
    inlines = [AnswerInline,]
    
class TestAdmin(nested_admin.NestedModelAdmin):
	inlines = [QuestionInline,]
    
class StudentAnswerInline(admin.TabularInline):
	model = StudentAnswer
	extra = 0

class StudentAdmin(admin.ModelAdmin):
	inlines = [StudentAnswerInline,]


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
#admin.site.register(AnswerVV)
admin.site.register(Student,StudentAdmin)
admin.site.register(StudentAnswer)
admin.site.register(AudioAnswer)

#class QuestionAdmin(admin.ModelAdmin):
#    """list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
#    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]"""
#    inlines = [AnswerInline]
#    
#admin.site.register(Question, QuestionAdmin)
#
#class QuestionInline(admin.TabularInline):
#    model = Question
#    extra = 0
#class TestAdmin(admin.ModelAdmin):
#    """list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
#    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]"""
#    inlines = [QuestionInline]
    