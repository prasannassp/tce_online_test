from django.contrib import admin
from .models import User, Question, TakenQuiz, Quiz, Subject, Answer, Student, StudentAnswer

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Answer)
admin.site.register(Quiz)
