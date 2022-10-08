from django.contrib import admin
from .models import Course_List, Course_Summary, Ana_Quiz, Ana_Question, Ana_Answer

# Register your models here.
admin.site.register(Course_List)
admin.site.register(Course_Summary)
admin.site.register(Ana_Quiz)

class AnswerInLineTable(admin.TabularInline):
    model = Ana_Answer
    fields = [
        'choice',
        'correct',
    ]

class Ana_QuestionAdmin(admin.ModelAdmin):
    fields = [
        'quiz',
        'question',
    ]
    list_display = [
        'quiz',
        'question',
    ]
    inlines = [
        AnswerInLineTable,
    ]

class Ana_AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'choice',
        'correct'
    ]

admin.site.register(Ana_Question, Ana_QuestionAdmin)
admin.site.register(Ana_Answer, Ana_AnswerAdmin)
