from django.contrib import admin
from .models import Survey, Question, Answer, Response


class QuestionInline(admin.StackedInline):
    model = Question


class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionInline,]
    list_display = ('title', 'description')
    search_fields = ('title',)


'''class AnswerInline(admin.StackedInline):
    model = Answer


class ResponseAdmin(admin.ModelAdmin):
    inlines = [AnswerInline,]
    list_display = ('answer',)
    search_fields = ('answer',)'''


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answer)
admin.site.register(Response)
