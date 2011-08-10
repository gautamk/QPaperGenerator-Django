#!/usr/bin/python
from django.contrib import admin
from QPaperGenerator.QP.models import *

class InlineSubjectAdmin(admin.TabularInline):
    model = Subject
    extra = 2

class DepartmentAdmin(admin.ModelAdmin):
    inlines = [InlineSubjectAdmin,]
    fields = ('name', 'description') 
    list_filter = ('name', )
    search_fields = ('name','description')

class QuestionInlineAdmin(admin.TabularInline):
    model = Question
    extra = 3

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name' , 'subject_code' , 'department' , )
    list_display_links = ('name' ,)
    list_editable = ('subject_code' , 'department')
    fields = ('department' , 'name' , 'subject_code' , 'description' , )
    list_filter = ( 'department' , 'name' , 'subject_code' , )
    search_fields = ('name', 'department' , 'subject_code' , 'description')
    inlines = [QuestionInlineAdmin]
    pass
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question' , 'question_type' , 'unit_number', 'subject' )
    list_display_links = ('question' ,)
    list_editable = ('question_type' ,'unit_number' ,  'subject')
    list_filter = ('question_type' , 'unit_number' , 'subject')
    pass 

admin.site.register(Department , DepartmentAdmin)
admin.site.register(Subject , SubjectAdmin)
admin.site.register(Question , QuestionAdmin)  
